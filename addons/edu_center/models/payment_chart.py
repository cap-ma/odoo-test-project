from odoo import models, fields, api
import json

class PaymentChart(models.Model):
    _name = 'educational.payment.chart'
    _description = 'Payment Chart'

    chart_start_date = fields.Date(string='Start Date')
    chart_end_date = fields.Date(string='End Date')
    chart_data = fields.Text(string='Chart Data', compute='_compute_chart_data', store=True)

    @api.depends('chart_start_date', 'chart_end_date')
    def _compute_chart_data(self):
        for record in self:
            if record.chart_start_date and record.chart_end_date:
                data = self.get_payment_data(record.chart_start_date, record.chart_end_date)
                record.chart_data = json.dumps(data)
            else:
                record.chart_data = '[]'

    def load_chart_data(self):
        self.ensure_one()
        self._compute_chart_data()
        return {'type': 'ir.actions.client', 'tag': 'reload'}

    @api.model
    def get_payment_data(self, start_date, end_date):  
        payments = self.env['educational.teacher.payment'].read_group(
            [('date', '>=', start_date), ('date', '<=', end_date)],
            ['amount:sum', 'teacher_id'],
            ['teacher_id']
        )
        return [{'teacher_name': payment['teacher_id'][1], 'payment': payment['amount']} for payment in payments]