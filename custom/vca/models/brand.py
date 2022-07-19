from odoo import models, fields, api, _


class Brand(models.Model):
    _name = "vca.brand"
    _description = "Vca Brand"

    name = fields.Char(required=True)
    # certificate_ids = fields.One2many("vca.certificate", "brand_id", string="Certificates")