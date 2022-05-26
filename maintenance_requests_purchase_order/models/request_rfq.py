# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class RequestRfqMRCustom(models.Model):

    _name = 'request.rfq.mr.custom'
    _description = 'RFQ Line'
    _order = 'maintenance_request_id, id'

    maintenance_request_id = fields.Many2one('maintenance.request', string='Maintenance Request')
    sequence = fields.Integer(string='Sequence', default=10)
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict', required=True)
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True)
    product_uom_qty = fields.Float(string='Request Quantity', digits='Product Unit of Measure', required=True, default=1.0)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', required=True)
    qty_onhand = fields.Float(string="Quantity on Hand")
    custom_purchase_line_id = fields.Many2one('purchase.order.line',string="Purchase Order Line",copy=False,)
    custom_purchase_id = fields.Many2one('purchase.order',string="Purchase Order",copy=False,related='custom_purchase_line_id.order_id')

    @api.onchange('product_id')
    def product_id_change(self):
        for rec in self:
            rec.product_uom = rec.product_id.uom_id.id
            if rec.product_id:
                rr = rec.product_id._compute_quantities_dict(lot_id=False, owner_id=False, package_id=False, from_date=False, to_date=False)
                rec.qty_onhand = rr[rec.product_id.id]['qty_available']
