# importing necessary files

from odoo import models, fields

class PartyTypes(models.Model):
    _name = 'party.types'
    _description = 'This model contains name of party types'

    name = fields.Char(required=True, help="Please mention party type")
    description = fields.Text()


    # defining sql constraints so that we cannot create multiple types with same name
    _sql_constraints = [
        (
            'check_unique_party_type_name',
            'unique (name)',
            'This name already exists. \nPlease provide unique name'
        )
    ]