from odoo import models, fields, api


class Group(models.Model):
    _name = 'educational.group'
    _description = 'Educational Group'

    name = fields.Char(string='Name', required=True)
    course_id = fields.Many2one('educational.course', string='Course', required=True)
    teacher_id = fields.Many2one('educational.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('educational.student', string='Students')
    payment_ids = fields.One2many('educational.payment', 'group_id', string='Payments')

    @api.depends('payment_ids.amount', 'payment_ids.state')
    def _compute_total_payments(self):
        for group in self:
            group.total_payments = sum(payment.amount for payment in group.payment_ids if payment.state == 'confirmed')

    total_payments = fields.Float(string='Total Payments', compute='_compute_total_payments', store=True)

    @api.model
    def add_students(self, student_ids):
        self.write({'student_ids': [(4, student_id) for student_id in student_ids]})
