# Importing necessary modules

from odoo import models, fields


class PartyPlanner(models.Model):
    _name = "party.planner"
    _description = "This model contains fields related to party planning odoo module"


    name = fields.Char(required=True)
    date = fields.Date(string="Date of Event", required=True) 
    attendees = fields.Integer(required=True, string="Total No of Attendees", default=1, help="This is taken for the purpose of the knowing beforehand how many people to manage")
    time = fields.Selection([('day', 'Day'), ('night', 'Night')], string="Party Time")
    # party type - many2one field 
    type_id = fields.Many2one('party.types', copy=False)
    # party tags - many2many field
    tag_ids = fields.Many2many('party.tags', copy=False) 
    # party plot address - many2one field 
    client_id = fields.Many2one('res.partner', copy=False)
    user_id = fields.Many2one('res.users')

    # city name - many2one field
    city_id = fields.Many2one('cities.cities')
    des = fields.Text(string="Additional Description")

