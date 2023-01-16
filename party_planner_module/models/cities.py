# importing necessary modules

from odoo import fields, models


class Cities(models.Model):
    _name = "cities.cities"
    _description = "This model contains Indian Cities Name"


    name = fields.Char(required=True, copy=False)
    
    # ordering the cities name acc to name
    _order = "name"