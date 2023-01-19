# Importing necessary modules

from odoo import models, fields

class PartyPlace(models.Model):
    _name = "party.place"
    _description = "This model contains party places for a particular city"


    name = fields.Char(required=True, copy=False)
    description = fields.Text()
    city_id = fields.Many2one(comodel_name="cities.cities")

    # adding sql constraints to check whether no two name equal
    _sql_constraints = [
        (
            'unique_party_place_name_check',
            'unique (name)',
            'This name already exists! Please enter a unique name'
        )
    ]