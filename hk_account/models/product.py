# -*- coding: utf-8 -*-
# Copyright: 2024 Hakika Strategy Into Action (Pty) Ltd

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    journal_ids = fields.Many2many('account.journal', 'account_journal_product_template_rel', string='Applicable Journals')
    project_applicable = fields.Boolean(string='Project Applicable')