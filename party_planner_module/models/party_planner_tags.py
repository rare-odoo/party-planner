# importing necessary modules 
from odoo import models, fields

class PartyTags(models.Model):
    _name = "party.tags"
    _description = "This model contains name and description of the parties"

    name = fields.Char(required=True)
    description = fields.Text()

    # defining constraints so that multiple same name cannot be created
    _sql_constraints = [
        (
            'check_unique_tag_name',
            'unique (name)',
            'This tag name already exists.\nPlease provide unique tag name'
        )
    ]