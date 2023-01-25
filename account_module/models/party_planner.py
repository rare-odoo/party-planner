from odoo import models, fields, api
from odoo import Command
from datetime import date

class InheritedPartyPlanner(models.Model):
    _inherit = 'party.planner'


    def invoice_generate_action(self):
        for record in self:
            self.env['account.move'].create({
                'partner_id': record.client_id.id,
                'invoice_date': date.today(),
                'move_type': 'out_invoice',
                'state': 'draft',
            })
        super().invoice_generate_action()