# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    maintenance_request_id = fields.Many2one(
        'maintenance.request', 
        string='Maintenance Request',
        copy=False,
    )