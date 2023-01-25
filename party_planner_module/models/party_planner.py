# Importing necessary modules
from datetime import date

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class PartyPlanner(models.Model):
    _name = "party.planner"
    _description = "This model contains fields related to party planning odoo module"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(required=True)

    # Adding state field which will give brief idea about the state of the event
    state = fields.Selection([("new","New"), ("validated","Validated"), ("progress", "In Progress"), ("done", "Done"), ("cancel", "Canceled")], default='new', tracking=True)

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
    user_id = fields.Many2one(comodel_name='res.users', tracking=True)

    # city name - many2one field
    city_id = fields.Many2one(comodel_name='cities.cities')
    des = fields.Text(string="Additional Description")


    # adding invoice generated boolean field just to check whether the invoice is generated or not
    invoice_generated = fields.Boolean(default=False)


    # food boolean field - through this field user can select whether they like to order food or not
    food = fields.Boolean(default=False)

    # food catering model one2many fields
    catering_order_ids = fields.One2many('catering.services', 'client_id')

    # defining rec_name using name_get method
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = "Parties " + str(record.id)
    #         result.append((record.id,name))
    #     return result

    # Adding Python Constraints to compare between today's date and date selected by the user
    # If it is before selected date then Raise Validation Error
    @api.constrains('date')
    def check_date(self):
        for record in self:
            if record.date < date.today():
                raise ValidationError("Please select a valid date!")


    # Action button definition
    # validation definition
    def validate_action_button(self):
        '''
            This button validate the quotation.
            It will be visible only if the quotation is new
            Once we press this button - the state changes to validated
        '''
        for record in self:
            record.state = 'validated'
    
    # send email definition
    def send_email_action_button(self):
        '''
            This button will send the user/partner the email template quotation.
            This button will not be visible if the quotation state is new or cancel
        '''
        pass

    # confirm action definition
    def confirm_action_button(self):
        '''
            If the admin wants to manually confirm the quotation then he can do it by clicking
            this button.
            This button changes the quotation state to inprogress
            This button will only be visible in validated state
        '''
        for record in self:
            record.state = 'progress'
    
    # cancel action definition
    def cancel_action_button(self):
        '''
            This button cancel's the quotation and changes the quotation state to cancel.
            This button will only be visible in validated state so once the quotation is validated
            it can be canceled through this
        '''
        for record in self:
            record.state = 'cancel'

    # invoice action definition
    def invoice_action_button(self):
        '''
            This button will generate the invoice for the current active quotation.
            Once the invoice is generated we can send it to customer/client
            This action button will also link the party planner module and the account module
        '''
        for record in self:
            record.invoice_generated = True

    # invoice share action
    def invoice_share_button(self):
        pass