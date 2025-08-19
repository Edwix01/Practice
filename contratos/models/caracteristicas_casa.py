from odoo import models, fields

class CaracteristicasCasa(models.Model):
    _name = "caracteristicas.casa"
    _description = "Modelo para con caracteristicas de una casa"
    name = fields.Char(string = "Caracteristica")
