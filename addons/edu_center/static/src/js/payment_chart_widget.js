/** @odoo-module **/

import { registry } from "@web/core/registry";
import { formView } from "@web/views/form/form_view";
import { FormController } from "@web/views/form/form_controller";
import { useEffect, useRef } from "@odoo/owl";

class PaymentChartController extends FormController {
    setup() {
        super.setup();
        this.chartRef = useRef("chart");

        useEffect(() => {
            this.renderChart();
        });
    }

    renderChart() {
        const chartData = this.model.root.data.chart_data;
        if (chartData) {
            try {
                const data = JSON.parse(chartData);
                // Load Google Charts
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(() => {
                    const dataTable = new google.visualization.DataTable();
                    dataTable.addColumn('string', 'Teacher');
                    dataTable.addColumn('number', 'Payment');
                    data.forEach(item => {
                        dataTable.addRow([item.teacher_name, item.payment]);
                    });

                    const options = {
                        title: 'Teacher Payments',
                        legend: { position: 'none' },
                        chart: {
                            title: 'Teacher Payments',
                            subtitle: 'in dollars (USD)'
                        },
                        bars: 'vertical',
                        height: 400,
                        width: '100%',
                        bar: { groupWidth: "95%" },
                    };

                    const chart = new google.visualization.ColumnChart(this.chartRef.el);
                    chart.draw(dataTable, options);
                });
            } catch (error) {
                console.error('Error parsing chart data:', error);
            }
        }
    }
}

export const PaymentChartFormView = {
    ...formView,
    Controller: PaymentChartController,
};

registry.category("views").add("payment_chart_form", PaymentChartFormView);