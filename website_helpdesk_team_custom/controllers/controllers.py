# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.addons.website_helpdesk_form.controller.main import WebsiteForm


class WebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(['/helpdesk/', '/helpdesk/<model("helpdesk.team"):team>'], type='http', auth="public", website=True)
    def website_helpdesk_teams(self, team=None, **kwargs):
        res = super(WebsiteHelpdesk, self).website_helpdesk_teams(team=team, **kwargs)

        search = kwargs.get('search')
        # For breadcrumb index: get all team
        teams = request.env['helpdesk.team'].search(
            ['|', '|', ('use_website_helpdesk_form', '=', True), ('use_website_helpdesk_forum', '=', True),
             ('use_website_helpdesk_slides', '=', True)], order="id asc")
        if not request.env.user.has_group('helpdesk.group_helpdesk_manager'):
            current_partner = request.env.user.partner_id
            if current_partner != request.env.ref('base.public_partner'):

                teams = teams.sudo().filtered(lambda team: team.website_published and team.project_id and team.project_id.partner_id and
                                                       team.project_id.partner_id == current_partner)
            else:
                # teams = teams.filtered(lambda team: team.website_published)
                return request.render("website_helpdesk.not_published_any_team")

        if not teams:
            return request.render("website_helpdesk.not_published_any_team")
        result = self.get_helpdesk_team_data(team or teams[0], search=search)
        # For breadcrumb index: get all team
        # result['teams'] = teams
        res.qcontext['team'] = result['team']
        res.qcontext['teams'] = teams
        return res

        # if not request.env.user.has_group('helpdesk.group_helpdesk_manager'):
        #     request.env['helpdesk.team'].search(
        #     for team in res.qcontext['teams']:
        #         if team.project_id and team.project_id.partner_id:
        #             if team.project_id.partner_id != request.env.user.partner_id.id:
        #                 res.qcontext['teams'].remove(team)
        #     if res.qcontext['team'] not in res.qcontext['teams']:
        #         res.qcontext['team'] = res.qcontext['teams'][1]
        #
        #
        #     s=0
        # return res


class WebsiteForm(WebsiteForm):

    @http.route('''/helpdesk/<model("helpdesk.team", "[('use_website_helpdesk_form','=',True)]"):team>/submit''', type='http', auth="user", website=True)
    def website_helpdesk_form(self, team, **kwargs):
        res = super(WebsiteForm, self).website_helpdesk_form(team=team, **kwargs)
        return res


