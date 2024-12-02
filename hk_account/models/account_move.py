# -*- coding: utf-8 -*-
# Copyright: 2024 Hakika Strategy Into Action (Pty) Ltd

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    project_id = fields.Many2one('project.project', string='Project', copy=False)
    product_ids = fields.Many2many(related='journal_id.product_ids')
    account_control_ids = fields.Many2many(related='journal_id.account_control_ids')
    project_visible = fields.Boolean(compute='_compute_project_visible')
    ask_approve = fields.Boolean(string='Ask for Approval', default=True)

    # Question #1
    @api.depends('company_id', 'invoice_filter_type_domain')
    def _compute_suitable_journal_ids(self):
        for record in self:
            journal_type = record.invoice_filter_type_domain or 'general'
            company = record.company_id or self.env.company
            record.suitable_journal_ids = self.env['account.journal'].search([
                ('type', '=', journal_type),
            ]).filtered(lambda journal: company in journal.allowed_company_ids)

    # Question #3
    def _compute_project_visible(self):
        for record in self:
            record.project_visible = True if record.line_ids.filtered(lambda line: line.product_id.project_applicable).ids else False

    def action_post(self):

        for record in self:
            # Question #7
            if record.line_ids.filtered(lambda line: line.balance == 0):
                raise UserError(_('Posting is not allowed for zero balance entries.'))

            # Question #8
            if record.journal_id.mandatory_invoice_attachment and not record.attachment_ids:
                raise UserError(_('Posting is not allowed without an invoice attachment.'))

            # Question #6
            if not self.env.user.has_group('hk_account.group_journal_entry_approve'):
                raise UserError(_('You are not allowed to post journal entries.'))

        return super(AccountMove, self).action_post()

    def _compute_hide_post_button(self):
        print('compute hide post button')
        res = super(AccountMove, self)._compute_hide_post_button()
        for record in self:
            if not self.env.user.has_group('hk_account.group_journal_entry_approve'):
                record.hide_post_button = True

    def action_ask_approve(self):
        for record in self:
            record.ask_approve = True
