from odoo import models, fields


class Teacher(models.Model):
    _name = 'educational.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    contact_info = fields.Text(string='Contact Information')
    course_ids = fields.Many2many('educational.course', string='Courses')
    group_ids = fields.One2many('educational.group', 'teacher_id', string='Groups')