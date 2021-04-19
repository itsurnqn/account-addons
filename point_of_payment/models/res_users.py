from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    default_pop_id = fields.Many2one(
        'pop.config', 
        string='Caja por defecto',
        help="Caja por defecto para el usuario.")