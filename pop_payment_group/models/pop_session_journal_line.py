# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PopSessionJournalLine(models.Model):
    _inherit = 'pop.session.journal.line'


    @api.model
    def create(self, vals):
        
        # vals["name"] = vals[]
        # import pdb; pdb.set_trace()
        payment_id = self.env["account.payment"].browse(vals["account_payment_id"])
        payment_id.name = payment_id.payment_group_id.display_name
        vals["name"] = payment_id.name
        # import pdb; pdb.set_trace()
        res = super().create(vals)

        return res