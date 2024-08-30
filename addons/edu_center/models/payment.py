from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta


class Payment(models.Model):
    _name = 'educational.payment'
    _description = 'Student Payment'

    student_id = fields.Many2one('educational.student', string='Student', required=True)
    group_id = fields.Many2one('educational.group', string='Group', required=True)
    check = fields.Char(string='Check')
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Payment Date', default=fields.Date.today)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], string='State', default='draft')
    is_last_7_days = fields.Boolean(compute='_compute_is_last_7_days')
    test = fields.Float(compute="_test", store=True)

    def _get_last_7_days_domain(self):
        print('it is printed----------------------------------')
        today = fields.Date.today()
        seven_days_ago = today - timedelta(days=7)
        return [('date', '>=', seven_days_ago)]
    
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
            
    def generate_receipt(self):
        return {
            'type': 'ir.actions.report',
            'report_name': 'edu_center.report_payment_receipt',
            'report_type': 'qweb-pdf',
            'data': {'payment_id': self.id},
        }
    
    def process_payment(self):
        if self.state == 'draft':
            self.state = 'confirmed'
            # Additional logic for payment processing (e.g., updating account balance)
        else:
            raise UserError('Only draft payments can be processed.')