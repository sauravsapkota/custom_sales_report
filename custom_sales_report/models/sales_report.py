from odoo import models, fields, api

class SalesReportWizard(models.TransientModel):
    _name = 'sales.report.wizard'
    _description = 'Sales Report Wizard'

    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)

    def generate_report(self):
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'customer_id': self.customer_id.id,
        }
        return self.env['report'].get_action(self, 'custom_sales_report.sales_report_template', data=data)


class SalesReport(models.AbstractModel):
    _name = 'report.custom_sales_report.sales_report_template'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('custom_sales_report.sales_report_template')
        docs = self.env['sale.order'].search([
            ('partner_id', '=', data['customer_id']),
            ('date_order', '>=', data['from_date']),
            ('date_order', '<=', data['to_date']),
        ])
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'data': data,
        }
        return report_obj.render('custom_sales_report.sales_report_template', docargs)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    source = fields.Char(string='Source')
