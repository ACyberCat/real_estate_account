from odoo import models, fields, api, exceptions

class EstateProperties(models.Model):
    _inherit = 'estate.properties'

    def action_sell(self):
        res = self.env["account.journal"].search([("type", "=","sale")], limit=1)
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.buyer_id,
                    "move_type": "out_invoice",
                    "journal_id": self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal().id,
                    "invoice_line_ids": [
                        (0, 0, {
                                "name": prop.name,
                                "quantity": 1.0,
                                "price_unit": prop.selling_price,
                        }, ), (0,0,
                            {
                                "name": "Administrative fees",
                                "quantity": 1.0,
                                "price_unit": 100.0,
                            },
                        ),
                    ],
                }
            )
        return res