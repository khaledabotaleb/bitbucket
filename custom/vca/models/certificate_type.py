from odoo import models, fields


class Type(models.Model):
    _name = "vca.type"
    _description = "vca Certificate Type"

    name = fields.Char(required=True)
    certificate_ids = fields.One2many("vca.certificate", "type_id", string="Certificates")
