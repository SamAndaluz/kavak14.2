# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Maintenance Requests with Purchase Order',
    'version' : '2.1.2',
    'price' : 29.0,
    'currency': 'EUR',
    'category': 'Manufacturing/Maintenance',
    'license': 'Other proprietary',
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/maintenance_requests_purchase_order/199',#'https://youtu.be/npzxgxmsfxA',
    'images': [
        'static/description/img.jpg',
    ],
    'summary' : 'Maintenance team to create a Purchase Order / Request for Quotation from Maintenance Requests.',
    'description': """
This app allows your maintenance team to create a Purchase Order / Request for Quotation from Maintenance Requests.
Main Features
    - Allow your user to create an RFQ / Purchase Order from Maintenance Requests for selected vendors.
    - Allow your user to see all created RFQ/Purchase Order from the smart button on the Maintenance Request Form.
    - RFQ will be created based on Vendors selected on products line on Maintenance Requests.(All products lines will be grouped by vendor and multiple RFQ will be created based on selected vendors.).
    - Maintenance Request references will be stored on RFQ / Purchase Order.
    - For more details please check below screenshots and watch the video.
    """,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'depends' : [
        'maintenance',
        'sales_team',
        'purchase',
        'stock'
    ],
    'support': 'contact@probuse.com',
    'data' : [
        'security/ir.model.access.csv',
        'views/maintenance_request_view.xml'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
