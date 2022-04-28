# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskStage(models.Model):
    _inherit = 'helpdesk.stage'

    stage_bg_color = fields.Char('Stage BG Color')
