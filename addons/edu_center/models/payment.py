from odoo import models, fields, api
from odoo.exceptions import UserError


class Payment(models.Model):
    _name = 'educational.payment'
    _description = 'Student Payment'

    student_id = fields.Many2one('educational.student', string='Student', required=True)
    group_id = fields.Many2one('educational.group', string='Group', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Payment Date', default=fields.Date.today)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], string='State', default='draft')

    @api.model
    def create(self, vals):
        payment = super(Payment, self).create(vals)
        return payment

    def action_confirm(self):
        for payment in self:
            if payment.state == 'draft':
                payment.state = 'confirmed'
            else:
                raise UserError('Only draft payments can be confirmed.')

    def action_draft(self):
        for payment in self:
            if payment.state == 'confirmed':
                payment.state = 'draft'
            else:
                raise UserError('Only confirmed payments can be set to draft.')