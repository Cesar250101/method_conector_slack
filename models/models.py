# -*- coding: utf-8 -*-

from odoo import models, fields, api
import slack


class ModuleName(models.Model):
    _inherit = 'res.company'

    token_slack = fields.Char(string='Token Slack')


class ModuleName(models.Model):
    _inherit = 'crm.team'

    canal_slack = fields.Char(string='Canal Slack')


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def action_confirm(self):
        MntNeto = self.company_id.currency_id._convert(self.amount_total, self.currency_id, self.company_id, self.date_order)        
        mensaje="Felicitaciones a "+ self.user_id.name +" por el cierre del negocio para el cliente "+ self.partner_id.name
        mensaje+=" por un valor de "+str(MntNeto)
        
        
        
        res = super(SaleOrder, self).action_confirm()
        client=slack.WebClient(token=self.company_id.token_slack)
        client.chat_postMessage(channel=self.team_id.canal_slack,text=mensaje)
        return res