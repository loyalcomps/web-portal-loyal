# -*- coding: utf-8 -*-

from odoo import models, fields, api



import time
from odoo import api, models, _
from odoo.exceptions import UserError
import datetime
from datetime import datetime


class ReportTimesheet(models.AbstractModel):
    _name = 'report.portal_timesheet_report.report_timesheets'

    def get_sale(self, data):

        lines = []
        sl = 0

        customer = data['form']['customer']

        if customer:

            query = '''

                                               select aa.partner_id as customer, 
		bb.total_hours as total_hours,
		aa.consumed_hours as consumed_hours,		
		(bb.total_hours-aa.consumed_hours) as balance
		from

(select sum(an.unit_amount) as consumed_hours ,an.partner_id from account_analytic_line as an 
	inner join project_project as p on p.id= an.project_id
	inner join sale_order as s on (s.id=p.sale_order_id)
	left join sale_order_line as sl on s.id=sl.order_id
	where an.task_id is not null 
 	and an.partner_id =%s
	group by an.partner_id) aa	
	
	left join
	
(select m.partner_id,sum(m.total_hours) as total_hours from

(select distinct s.id,s.partner_id,(sl.product_uom_qty) as total_hours
		from sale_order_line as sl
		left join sale_order as s on s.id=sl.order_id
		left join project_project as p on p.sale_order_id= s.id
		left join account_analytic_line as an on p.id= an.project_id
	where s.project_id=an.project_id or s.id=p.sale_order_id
	
	union
	 
	select distinct s.id,s.partner_id,(sl.product_uom_qty) as total_hours
		from sale_order_line as sl
		left join sale_order as s on s.id=sl.order_id
		left join project_project as p on p.id= s.project_id
		left join account_analytic_line as an on p.id= an.project_id
	where s.project_id=an.project_id or s.id=p.sale_order_id)as m
 where m.partner_id=%s
	group by m.partner_id)bb 
	on bb.partner_id=aa.partner_id 

                                  '''

            self.env.cr.execute(query, (
                customer,customer
            ))
            for row in self.env.cr.dictfetchall():
                sl += 1

                customer = row['customer'] if row['customer'] else " "
                total_hours = row['total_hours'] if row['total_hours'] else 0
                consumed_hours = row['consumed_hours'] if row['consumed_hours'] else 0
                balance = row['balance'] if row['balance'] else 0


                res = {
                    'sl_no': sl,
                    'customer': self.env['res.partner'].browse(customer).name if customer else " ",
                    'total_hours': total_hours if total_hours else 0.0,
                    'consumed_hours': consumed_hours if consumed_hours else 0.0,
                    'balance': balance if balance else 0.0,


                }

                lines.append(res)
        # return [records, total]
            if lines:
                return lines
            else:
                return []
        else:

            query = '''

                                                                       select aa.partner_id as customer, 
                                bb.total_hours as total_hours,
                                aa.consumed_hours as consumed_hours,		
                                (bb.total_hours-aa.consumed_hours) as balance
                                from

                        (select sum(an.unit_amount) as consumed_hours ,an.partner_id from account_analytic_line as an 
                            inner join project_project as p on p.id= an.project_id
                            inner join sale_order as s on (s.id=p.sale_order_id)
                            left join sale_order_line as sl on s.id=sl.order_id
                            where an.task_id is not null 
                            group by an.partner_id) aa	

                            left join

                        (select m.partner_id,sum(m.total_hours) as total_hours from
                        
                        (select distinct s.id,s.partner_id,(sl.product_uom_qty) as total_hours
		from sale_order_line as sl
		left join sale_order as s on s.id=sl.order_id
		left join project_project as p on p.sale_order_id= s.id
		left join account_analytic_line as an on p.id= an.project_id
	where s.project_id=an.project_id or s.id=p.sale_order_id
	
	union
	 
	select distinct s.id,s.partner_id,(sl.product_uom_qty) as total_hours
		from sale_order_line as sl
		left join sale_order as s on s.id=sl.order_id
		left join project_project as p on p.id= s.project_id
		left join account_analytic_line as an on p.id= an.project_id
	where s.project_id=an.project_id or s.id=p.sale_order_id)as m
                            group by m.partner_id)bb 
                            on bb.partner_id=aa.partner_id 

                                                          '''

            self.env.cr.execute(query, (

            ))
            for row in self.env.cr.dictfetchall():
                sl += 1

                customer = row['customer'] if row['customer'] else " "
                total_hours = row['total_hours'] if row['total_hours'] else 0
                consumed_hours = row['consumed_hours'] if row['consumed_hours'] else 0
                balance = row['balance'] if row['balance'] else 0

                res = {
                    'sl_no': sl,
                    'customer': self.env['res.partner'].browse(customer).name if customer else " ",
                    'total_hours': total_hours if total_hours else 0.0,
                    'consumed_hours': consumed_hours if consumed_hours else 0.0,
                    'balance': balance if balance else 0.0,

                }

                lines.append(res)
            # return [records, total]
            if lines:
                return lines
            else:
                return []

    # if customer:
        #
        #     query = '''
        #
        #           select to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date as saledate,
        #                       pt.name as product_name,p.id as product_id,pt.list_price,sum(sl.product_uom_qty) as qty,
        #                       sum(sl.price_tax) as tax,sum(sl.price_total) as total_amount,sum(sl.price_subtotal) as untax_amount
        #                        from sale_order_line as sl
    	# 				left join sale_order as s on (sl.order_id=s.id)
    	# 				left join product_product as p on (sl.product_id=p.id)
    	# 				left join product_template as pt on (pt.id=p.product_tmpl_id)
        #
    	# 				where
        #                     s.state in  ('sale') and pt.own_product=true
        #                     and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
        #                     and s.operating_unit_id= %s group by s.date_order,p.id,pt.id
        #                     order by s.date_order
        #                    '''
        #
        #     self.env.cr.execute(query, (
        #         date_from, date_to, operating_unit
        #     ))
        #     for row in self.env.cr.dictfetchall():
        #         sl += 1
        #
        #         saledate = row['saledate'] if row['saledate'] else " "
        #         product_name = row['product_name'] if row['product_name'] else " "
        #         list_price = row['list_price'] if row['list_price'] else " "
        #         qty = row['qty'] if row['qty'] else " "
        #
        #         untax_amount = row['untax_amount'] if row['untax_amount'] else " "
        #         tax = row['tax'] if row['tax'] else 0
        #         total_amount = row['total_amount'] if row['total_amount'] else 0
        #
        #         sale_new_date = datetime.strptime(str(saledate), '%Y-%m-%d').date().strftime('%d-%m-%Y')
        #
        #
        #         res = {
        #             'sl_no': sl,
        #             'saledate': sale_new_date,
        #             'product_name': product_name if product_name else " ",
        #             'list_price': list_price if list_price else 0.0,
        #             'qty': qty if qty else 0.0,
        #             'untax_amount': untax_amount if untax_amount else 0.0,
        #             'tax': tax if tax else 0.0,
        #             'total_amount': total_amount if total_amount else 0.0
        #
        #         }
        #
        #         lines.append(res)
        # def get_timesheets(self, docs):
        #     """input : name of employee and the starting date and ending date
        #     output: timesheets by that particular employee within that period and the total duration"""

            # lines = []
            #
            # customer = data['form']['customer']
            #
            # Timesheet_sudo = self.env['account.analytic.line'].sudo()
            # # values = self._prepare_portal_layout_values()
            # domain = self.env['account.analytic.line']._timesheet_get_portal_domain()
            #
            # timesheets = Timesheet_sudo.search(domain)
            #
            # grouped_timesheets = [timesheets]
            #
            # # values.update({
            # #     'timesheets': timesheets,
            # #     'grouped_timesheets': grouped_timesheets,
            # # })
            #
            # if docs.customer:
            #     rec = self.env['account.analytic.line'].search(
            #         [('partner_id', '=', docs.customer[0].id), ('task_id', '=', False)])
            # else:
            #     rec = self.env['account.analytic.line'].read_group(
            #         [('partner_id', '=', docs.customer[0].id), ('task_id', '=', False)], group_by=['partner_id'])
            #
            # records = []
            # total = 0
            # for r in rec:
            #     vals = {
            #         # 'project': r.project_id.name,
            #         #     'user': r.user_id.partner_id.name,
            #         #     'duration': r.unit_amount,
            #         #     'date': r.date,
            #         'grouped_timesheets': grouped_timesheets,
            #
            #     }
            #     total += r.unit_amount
            #     lines.append(vals)
            # # return [records, total]
            # if lines:
            #     return lines
            # else:
            #     return []


    def _get_report_values(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_ids', []))

        customer = data['form']['customer']

        get_sale = self.get_sale(data)

        # date_object_startdate = datetime.strptime(date_from, '%Y-%m-%d').date()
        # date_object_enddate = datetime.strptime(date_to, '%Y-%m-%d').date()

        docargs = {
            'doc_ids': docids,
            'doc_model': self.model,
            'data': data['form'],
            # 'date_start': date_object_startdate.strftime('%d-%m-%Y'),
            # 'date_end': date_object_enddate.strftime('%d-%m-%Y'),
            'docs': docs,
            'time': time,
            'grouped_timesheets': get_sale,
            'customer':customer,
        }
        return docargs



# class ReportTimesheet(models.AbstractModel):
#     _name = 'report.portal_timesheet_report.report_timesheets'

    # def get_timesheets(self, docs):
    #     """input : name of employee and the starting date and ending date
    #     output: timesheets by that particular employee within that period and the total duration"""
    #
    #     Timesheet_sudo = self.env['account.analytic.line'].sudo()
    #     # values = self._prepare_portal_layout_values()
    #     domain = self.env['account.analytic.line']._timesheet_get_portal_domain()
    #
    #     timesheets = Timesheet_sudo.search(domain)
    #
    #     grouped_timesheets = [timesheets]
    #
    #     # values.update({
    #     #     'timesheets': timesheets,
    #     #     'grouped_timesheets': grouped_timesheets,
    #     # })
    #
    #
    #     if docs.customer:
    #         rec = self.env['account.analytic.line'].search([('partner_id', '=', docs.customer[0].id),('task_id','=',False)])
    #     else:
    #         rec = self.env['account.analytic.line'].read_group([('partner_id', '=', docs.customer[0].id),('task_id','=',False)],group_by=['partner_id'])
    #
    #
    #     records = []
    #     total = 0
    #     for r in rec:
    #         vals = {
    #             # 'project': r.project_id.name,
    #             #     'user': r.user_id.partner_id.name,
    #             #     'duration': r.unit_amount,
    #             #     'date': r.date,
    #                 'grouped_timesheets': grouped_timesheets,
    #
    #                 }
    #         total += r.unit_amount
    #         records.append(vals)
    #     return [records, total]

    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     """we are overwriting this function because we need to show values from other models in the report
    #     we pass the objects in the docargs dictionary"""
    #     docs = self.env['portal.timesheet.wizard'].browse(self.env.context.get('active_id'))
    #     identification = []
    #     for i in self.env['res.partner'].search([('id', '=', docs.customer[0].id)]):
    #         if i:
    #             identification.append({'id': i.id, 'name': i.name})
    #     timesheets = self.get_timesheets(docs)
    #     company_name = self.env['res.company'].search([('name', '=', docs.customer[0].company_id.name)])
    #     period = None
    #
    #     Timesheet_sudo = self.env['account.analytic.line'].sudo()
    #     # values = self._prepare_portal_layout_values()
    #     domain = self.env['account.analytic.line']._timesheet_get_portal_domain()
    #
    #     timesheets = Timesheet_sudo.search(domain)
    #
    #     grouped_timesheets = [timesheets]
    #
    #     if len(identification) > 1:
    #         return {
    #             'doc_ids': self.ids,
    #             # 'doc_model': self.model,
    #             'docs': docs,
    #             'timesheets': timesheets[0],
    #             'total': timesheets[1],
    #             'company': company_name,
    #             'identification': identification,
    #             'period': period,
    #             # 'timesheets': timesheets,
    #             'grouped_timesheets': grouped_timesheets,
    #         }
    #     else:
    #         return {
    #             'doc_ids': self.ids,
    #             # 'doc_model': self.model,
    #             'docs': docs,
    #             'timesheets': timesheets[0],
    #             'total': timesheets[1],
    #             'identification': identification,
    #             'company': company_name,
    #             'period': period,
    #             # 'timesheets': timesheets,
    #             'grouped_timesheets': grouped_timesheets,
    #         }
