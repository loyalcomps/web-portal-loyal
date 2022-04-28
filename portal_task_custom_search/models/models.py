# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    stage_bg_color = fields.Char('Stage BG Color')
