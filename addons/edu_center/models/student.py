from odoo import models, fields, api


class Student(models.Model):
    _name = 'educational.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    contact_info = fields.Text(string='Contact Information')
    group_ids = fields.Many2many('educational.group', string='Groups')
    payment_ids = fields.One2many('educational.payment', 'student_id', string='Payments')


    @api.depends('payment_ids.amount', 'payment_ids.state')
    def _compute_total_fees(self):
        for student in self:
            student.total_fees = sum(payment.amount for payment in student.payment_ids if payment.state == 'confirmed')

    total_fees = fields.Float(string='Total Fees', compute='_compute_total_fees', store=True)

   