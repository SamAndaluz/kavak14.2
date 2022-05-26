# -*- coding: utf-8 -*-
{
    'name': "ITL Approvals General",

    'summary': """
        Este módulo agrega cambios en los tipos de aprobación, tales como:
        - Agregar soporte para crear aprobaciones por departamentos.
        - Agrega cambios en común para las aprobaciones.""",

    'description': """
        Este módulo agrega cambios en los tipos de aprobación, tales como:
        - Agregar soporte para crear aprobaciones por departamentos.
        - Agrega cambios en común para las aprobaciones.
    """,

    'author': "ITlighten",
    'website': "https://www.itlighten.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','approvals','hr_holidays'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/approval_category_views.xml',
        'views/approval_request_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
