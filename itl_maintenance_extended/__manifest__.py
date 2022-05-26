{

    # App information
    'name': 'ITL Maintenance Extended',
    'category': 'Manufacturing/Maintenance',
    'version': '15.0.0',
    'summary': '',
    'description': """
        """,

    # Dependencies
    'depends': ['maintenance'],

    'data': [
        'views/equipment_views.xml',
        'report/equipment_reports.xml',
        'report/equipment_templates.xml',
    ],

    'qweb': [
    ],

    # Odoo Store Specific
    'images': [],

    # Author
    'author': 'ITLighten',
    'website': 'https://www.itlighten.com',
    'maintainer': 'itlighten.com',

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
