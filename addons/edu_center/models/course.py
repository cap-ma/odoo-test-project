from odoo import models, fields

class Course(models.Model):
    _name = 'educational.course'
    _description = 'Educational Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    teacher_ids = fields.Many2many('educational.teacher', string='Teachers')
    group_ids = fields.One2many('educational.group', 'course_id', string='Groups')