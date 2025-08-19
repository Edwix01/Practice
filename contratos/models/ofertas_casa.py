from odoo import models, fields,api

class OfertasCasa(models.Model):
    _name = "ofertas.casa"
    _description = "Modelo para con las ofertas disponibles"
   
    price = fields.Float()
    state = fields.Selection([
        ("accepted","Accepted"),
        ("refused","Refused"),
    ], string="Status", copy=False)
    partner_id = fields.Many2one(comodel_name = "res.partner",required = True)
    casa_id = fields.Many2one(comodel_name = "contratos.casa",required = True)

