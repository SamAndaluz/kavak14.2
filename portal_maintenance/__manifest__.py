# -*- coding: utf-8 -*-

{
    'name': 'Portal Maintenance Request',
    'version': '1.0',
    'author': "Rozy Consultant.",
    'category': 'HR',
    'depends': ['maintenance','portal'],
    'description': """ Maintenance request from portal side""",
    'summary': """Manage maintenance request from portal side""",
    "data": [
        'security/ir.model.access.csv',
        'views/maintenance.xml',
        'views/maintenance_form_view.xml',
    ],
    'images': ['static/description/main_screen.jpeg'],
    'currency': 'EUR',
    'price': 100,
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
