# Importing necessary modules

from odoo import models, fields


class PartyPlanner(models.Model):
    _name = "party.planner"
    _description = "This model contains fields related to party planning odoo module"


    name = fields.Char(required=True)
    date = fields.Date(string="Date of Event") 
    attendees = fields.Integer(required=True, string="Total No of Attendees", default=1, help="This is taken for the purpose of the knowing beforehand how many people to manage")
    time = fields.Selection([('day', 'Day'), ('night', 'Night'), ('noon', 'Noon')], string="Party Schedule")
    # party type - many2one field 
    type_id = fields.Many2one(comodel_name='party.types', copy=False)
    # party tags - many2many field
    tag_ids = fields.Many2many(comodel_name='party.tags', copy=False) 
    # party plot address - many2one field 
    place_id = fields.Many2one(comodel_name="party.place",  domain="[('city_id','=',city_id)]")


    client_id = fields.Many2one(comodel_name='res.partner', copy=False)
    user_id = fields.Many2one(comodel_name='res.users')

    # city name - many2one field
    city_id = fields.Many2one(comodel_name='cities.cities')
    des = fields.Text(string="Additional Description")

    # defining rec_name using name_get method
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = "Parties " + str(record.id)
    #         result.append((record.id,name))
    #     return result

        