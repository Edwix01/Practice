from odoo import models, fields,api

class ContratosCasa(models.Model):
    _name = "contratos.casa"
    _description = "Modelo para gestionar los contratos de la casa"
    
    name = fields.Char(required = True, string = "Nombre")
    type_casa = fields.Many2one(comodel_name='tipos.casa')
    description = fields.Text(required = True, string = "Descripción",default='Come to meet the greatest view an apartment can be havel right in the center NY')
    postcode = fields.Char(string = "Código Postal")
    active = fields.Boolean(default=True)
    state = fields.Selection(selection = [("new","New"),("offer received", "offer received")],default = "new", string = 'Status')
    date_availability = fields.Date(copy=True,string = "Fecha de Disponibilidad",default=lambda self: fields.Date.add(fields.Date.today(),months=5))
    expected_price = fields.Float(string = "Precio Esperado")
    selling_price = fields.Float(string = "Precio de Venta",readonly=True)
    bedrooms = fields.Integer(string = "Habitaciones",default = 2)
    living_area = fields.Integer(string = "Living Area (sqm)")
    facades = fields.Integer(string = "Fachadas")
    garages = fields.Boolean(string = "Garaje",default = False)
    garden = fields.Boolean(string = "Jardín")
    garden_area = fields.Integer(string = "Area del Jardín")
    #El formato selection funciona de esta forma: selection = [('valor1','texto a presentarse'),...] 
    garden_orientation = fields.Selection(selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')])
    buyer_id = fields.Many2one(comodel_name='res.partner',ondelete = 'restrict') 
    salesperson_id = fields.Many2one(comodel_name='res.users',ondelete = 'restrict')
    caracteristicas = fields.Many2many(comodel_name='caracteristicas.casa',ondelete = 'restrict')
    ofertas = fields.One2many(comodel_name="ofertas.casa",inverse_name="casa_id")
    best_offer = fields.Integer(compute="_compute_best_offer")


    @api.depends("ofertas.price")
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.ofertas.mapped("price"),default=0)
