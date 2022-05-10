# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Task(models.Model):
    _inherit = "project.task"

    description = fields.Html(string='Description', required=True)
    development_time = fields.Float("Development Time", tracking=True)
    implementation_time = fields.Float("Implementation Time", tracking=True)

    @api.constrains('planned_hours', 'name')
    def _check_planned_hours(self):
        for task in self:
            if task.planned_hours <= 0:
                raise ValidationError(_('Planned hour must be greater than 0 '))

    @api.onchange('development_time', 'implementation_time')
    def calculate_planned_hour(self):
        for task in self:
            task.planned_hours = task.development_time + task.implementation_time


