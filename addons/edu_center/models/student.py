from odoo import models, fields


class Student(models.Model):
    _name = 'educational.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    contact_info = fields.Text(string='Contact Information')
    group_ids = fields.Many2many('educational.group', string='Groups')
    payment_ids = fields.One2many('educational.payment', 'student_id', string='Payments')

