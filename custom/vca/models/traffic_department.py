from odoo import models, fields, api, _


class TrafficDepartment(models.Model):
    _name = "vca.department"
    _description = "Vca Traffic Department"

    name = fields.Char(required=True)
    # certificate_ids = fields.One2many("vca.certificate", "department_id", string="Certificates")