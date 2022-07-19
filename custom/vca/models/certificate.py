import datetime

from odoo import models, fields, api, _


class VcaCertificate(models.Model):
    _name = "vca.certificate"
    _description = "Vca Certificate"

    def dynamic__years_selection(self):
        current_year = datetime.datetime.today().year
        YEARS = [(current_year - i, current_year - i) for i in range(20)]
        return YEARS

    serial_number = fields.Char(string='Number', required=True,
                               readonly=True, default=lambda self: _('New'))
    type_id = fields.Many2one("vca.type")
    brand_field = fields.Many2one("vca.brand")
    traffic_department = fields.Many2one("vca.department")
    vehicle_type = fields.Selection(
        [("c", "Car"), ("b", "Bus"), ("mb", "MiniBus"), ("m", "Microbus"),],
        default="c"
    )
    car_model = fields.Selection(dynamic__years_selection, string='Car Models')
    customer = fields.Many2one("res.partner")
    motor_number = fields.Char()
    chassis_number = fields.Char()
    price = fields.Float()

    @api.model
    def create(self, vals):
        if vals.get('serial_number', _('New')) == _('New'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code(
                'vca.certificate') or _('New')
        res = super(VcaCertificate, self).create(vals)
        return res