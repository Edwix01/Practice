from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Property Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Availability Date')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms', default=0)
    living_area = fields.Float(string='Living Area (sqm)', default=0.0)
    facades = fields.Integer(string='Facades', default=0)
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Float(string='Garden Area (sqm)', default=0.0)
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),       
        ('cancelled', 'Cancelled')
    ], string='State', default='new')       