from odoo import models, fields

class TiposCasa(models.Model):
    _name = "tipos.casa"
    _description = "Modelo para con tipo de casas existentes"
    name = fields.Char(string = "Tipo de Casa")
