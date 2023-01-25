# importing necessary files 
from odoo import api, fields, models

class CateringServices(models.Model):
    _name = "catering.services"
    _description = "This model contains all the necessary information about the food and beverages catering services"


    name = fields.Char(required=True)
    date = fields.Date()
    time = fields.DateTime()
    client_id = fields.Many2one('party.planner')