# -*- coding: utf-8 -*-
# Copyright: 2024 Hakika Strategy Into Action (Pty) Ltd

from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # Question #4
    @api.model_create_multi
    def create(self, vals):
        record = super(AccountMoveLine, self).create(vals)
        for res in record:
            if res.move_id and res.account_id != res.move_id.journal_id.default_counter_account_id:
                res.copy({
                    'move_id': res.move_id.id,
                    'account_id': res.move_id.journal_id.default_counter_account_id.id,
                    'debit': res.credit,
                    'credit': res.debit,
                    'balance': res.balance*-1,
                    'amount_currency': res.amount_currency*-1,
                })
        return record