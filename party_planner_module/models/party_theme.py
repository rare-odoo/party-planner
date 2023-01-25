# importing necessary modules 
from odoo import fields, models

class PartyTheme(models.Model):
    _name = "party.theme"
    _description = "This model contains party theme details"

    name = fields.Char(required=True)
    type_id = fields.Many2one(comodel_name="party.types")
    description = fields.Text()


    # Adding sql constraints to check unique name for the name fields
    _sql_constraints = [
        (
            'check_unique_theme_name',
            'unique (name)',
            'This name already exists! Please enter a unique name'
        )
    ]