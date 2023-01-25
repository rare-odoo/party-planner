# Inheriting res user 
from odoo import fields, models

class InheritedModel(models.Model):
    _inherit = "res.users"


    assigned_party_ids = fields.One2many("party.planner", "user_id", domain=[('state', '=', 'validated')]) 