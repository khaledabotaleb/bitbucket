from odoo import models, fields, api, _


class CustomerInherit(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(required=True)
    phone_number = fields.Char(required=True)

