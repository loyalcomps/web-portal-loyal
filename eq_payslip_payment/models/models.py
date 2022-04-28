# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import Warning


class emp_payslip_payment(models.TransientModel):
    _name = 'emp.payslip.payment'
    _description = 'Employee Payslip Payment'

    payment_date = fields.Date(string="Payment Date", default=fields.date.today())
    emp_payslip_payment_lines = fields.One2many('emp.payslip.payment.line', 'emp_payslip_payment_id', string="Payment Line", copy=False)
    journal_id = fields.Many2one('account.journal', string="Payment Journal")

    @api.model
    def default_get(self, fields):
        res = super(emp_payslip_payment, self).default_get(fields)
        if self._context.get('payslip_ids') and self._context.get('active_model') == 'hr.payslip':
            payslip_lst = []
            payslip_ids = self.env['hr.payslip'].browse(self._context.get('payslip_ids'))
            for payslip in payslip_ids.filtered(lambda l:l.state == 'done'):
                due_amount = sum(payslip.payment_move_ids.filtered(lambda l:l.state == 'posted').mapped('amount_total'))
                payment_lines = {'employee_id': payslip.employee_id.id,
                                 'number': payslip.number,
                                 'payslip_id': payslip.id,
                                 'payslip_due_amount': (payslip.pay_amount - due_amount),
                                 'company_id': payslip.company_id.id,
                                 'paid_amount': (payslip.pay_amount - due_amount),
                                 'currency_id':payslip.company_id.currency_id.id}
                payslip_lst.append((0, 0, payment_lines))
            res.update({'emp_payslip_payment_lines': payslip_lst})
        return res

    def do_confirm_payslip_payment(self):
        if not self.emp_payslip_payment_lines:
            raise Warning(_('No payment lines found.'))
        for line in self.emp_payslip_payment_lines.filtered(lambda l:l.payslip_id):
            if not line.journal_id:
                raise Warning(_('Please configured payment journal in payment lines.'))
            if line.payslip_due_amount < 0:
                raise Warning(_('Payslip due amount should be positve.'))
            if line.paid_amount <= 0:
                raise Warning(_('Please enter payslip paid amount.'))
            if not line.journal_id.default_credit_account_id:
                raise Warning(_("Please Configured Payment Journal Credit Account!"))
            line.generate_payment_move()

    @api.onchange('journal_id')
    def onchange_journal_id(self):
        if self.journal_id:
            for line in self.emp_payslip_payment_lines:
                line.journal_id = self.journal_id.id


class emp_payslip_payment_line(models.TransientModel):
    _name = 'emp.payslip.payment.line'
    _description = 'employee payslip payment line'

    emp_payslip_payment_id = fields.Many2one('emp.payslip.payment', string="Payslip Payment")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    paid_amount = fields.Monetary(string="Amount To Pay")
    payslip_due_amount = fields.Monetary(string="Due Amount")
    payslip_id = fields.Many2one('hr.payslip', string="Payslip")
    journal_id = fields.Many2one('account.journal', string="Payment Journal")
    company_id = fields.Many2one('res.company', string="Company")
    currency_id = fields.Many2one('res.currency', string="Currency", store=True)
    number = fields.Char(string="Reference")

    def generate_payment_move(self):
        self.ensure_one()
        move_lines = []
        payslip_id = self.payslip_id

        if payslip_id.journal_id and not payslip_id.journal_id.default_credit_account_id:
            raise Warning(_('Payslip Salary Journal "%s" should be configured Credit Account.!') % (payslip_id.journal_id.name))

        credit_note = payslip_id.credit_note
        name = 'Pay Salary'
        payslip_name = payslip_id.name
        credit_account_id = self.journal_id.default_credit_account_id.id
        debit_account_id = payslip_id.journal_id.default_debit_account_id.id
        credit_vals = {
            'name': name if not credit_note else payslip_name,
            'debit': 0.0,
            'credit': abs(self.paid_amount),
            'account_id': credit_account_id if not credit_note else debit_account_id,
        }
        move_lines.append((0, 0, credit_vals))
        debit_vals = {
                'name': payslip_name if not credit_note else name,
                'debit': abs(self.paid_amount),
                'credit': 0.0,
                'account_id': debit_account_id if not credit_note else credit_account_id,
            }
        move_lines.append((0, 0, debit_vals))
        vals = {
            'journal_id': self.journal_id.id,
            'date': self.emp_payslip_payment_id.payment_date or fields.date.today(),
            'line_ids': move_lines,
            'ref': payslip_id.number,
        }
        move = self.env['account.move'].sudo().create(vals)
        move.post()
        payslip_id.payment_move_ids += move
        total_payments = sum(payslip_id.payment_move_ids.mapped('amount_total'))
        if total_payments >= payslip_id.pay_amount:
            payslip_id.state = 'paid'
        return True


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    @api.depends('line_ids')
    def compute_pay_amount(self):
        for rec in self:
            pay_amount = sum(rec.line_ids.filtered(lambda l:l.category_id.code == 'NET').mapped('total')) or 0.00
            rec.pay_amount = pay_amount

    pay_amount = fields.Float('Payable Amount', compute='compute_pay_amount', store=True)
    payment_move_ids = fields.Many2many('account.move', string="Journal Entries", copy=False)
    state = fields.Selection(selection_add=[('paid', 'Paid')])

    def compute_sheet(self):
        for payslip in self:
            payslip.compute_pay_amount()
        return super(hr_payslip, self).compute_sheet()

    def action_view_entries(self):
        self.ensure_one()
        action = self.env.ref('account.action_move_journal_line').read()[0]
        action['domain'] = [('id', 'in', self.payment_move_ids.ids)]
        action['context'] = {}
        return action

    def wizard_payslip_payment(self):
        due_amount = sum(self.payment_move_ids.filtered(lambda l:l.state == 'posted').mapped('amount_total'))
        payment_lines = [{'employee_id':self.employee_id.id, 'payslip_id':self.id,
                          'number': self.number,
                          'payslip_due_amount':(self.pay_amount - due_amount),
                          'company_id':self.company_id.id,
                          'currency_id':self.company_id.currency_id.id,
                          'paid_amount':(self.pay_amount - due_amount)}]
        ctx = {'default_company_id': self.company_id.id,
               'default_emp_payslip_payment_lines': payment_lines}
        return {
            'name': 'Payslip Payment',
            'type': 'ir.actions.act_window',
            'res_model': 'emp.payslip.payment',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context':ctx
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: