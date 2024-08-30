from odoo import models, fields


class TeacherPayment(models.Model):
    _name = 'educational.teacher.payment'
    _description = 'Teacher Payment'

    teacher_id = fields.Many2one('educational.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Payment Date', default=fields.Date.today)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], string='State', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_draft(self):
        self.state = 'draft'