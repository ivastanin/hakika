# -*- coding: utf-8 -*-
# Copyright: 2024 Hakika Strategy Into Action (Pty) Ltd

from odoo import fields, models



class AccountJournal(models.Model):
    _inherit = "account.journal"

    allowed_company_ids = fields.Many2many('res.company', string='Allowed Companies')
    default_counter_account_id = fields.Many2one('account.account', string='Default Counter Account')
    product_ids = fields.Many2many('product.template', 'account_journal_product_template_rel', string='Applicable Products')
    mandatory_invoice_attachment = fields.Boolean(string='Mandatory Invoice Attachment')
