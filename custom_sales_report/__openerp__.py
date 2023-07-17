{
    'name': 'Custom Sales Report',
    'version': '1.0',
    'author': 'Saurav Sapkota',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_report_view.xml',
        'report/sales_report_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}