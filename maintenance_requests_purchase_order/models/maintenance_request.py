# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class MaintenanceRrequest(models.Model):
    _inherit = 'maintenance.request'

    def _custom_purchase_order_count(self):
        PurchaseOrder = self.env['purchase.order']
        for rec in self:
            rec.purchase_order_count = PurchaseOrder.search_count([('maintenance_request_id', '=', rec.id)])

    purchase_order_count = fields.Integer(compute='_custom_purchase_order_count', string='of RFQ(s)')
    request_rfq_line = fields.One2many('request.rfq.mr.custom', 'maintenance_request_id', 'Product Request')
    purchase_order_ids = fields.One2many('purchase.order', 'maintenance_request_id', 'Purchase Order')

    def custom_open_rfq(self):
        for rec in self:
            rfq_ids = self.env['purchase.order'].search([
                ('maintenance_request_id', '=', rec.id)
            ])
            result = self.env.ref('purchase.purchase_rfq')
            action_ref = result or False
            result = action_ref.sudo().read()[0]
            result['domain'] = str([('id', 'in', rfq_ids.ids)])
            return result

    def create_rfq(self):
        for rec in self:
            purchase_obj = self.env['purchase.order']
            purchase_line_obj = self.env['purchase.order.line']
            supplier_dict= {}

            for request in rec.request_rfq_line:
                if request.partner_id:
                    if request.partner_id not in supplier_dict:
                        supplier_dict[request.partner_id] = [request]
                    else:
                        supplier_dict[request.partner_id].append(request)
                else:
                    raise UserError(_("Please set Supplier"))

            rfq_list = []
            for supp in supplier_dict:
                purchase_dict = {'partner_id':supp.id, 'origin':rec.name, 'maintenance_request_id': rec.id}
                purchase_order = purchase_obj.create(purchase_dict)
                rfq_list.append(purchase_order.id)
                for request in supplier_dict[supp]:
                    if not request.custom_purchase_line_id:
                        lines = {
                            'product_id':request.product_id.id,
                            'product_qty':request.product_uom_qty,
                            'product_uom':request.product_uom.id,
                            'price_unit':request.product_id.standard_price,
                            'name':request.product_id.name,
                            'date_planned': datetime.today(),
                            'order_id': purchase_order.id,
                        }
                        line = purchase_line_obj.create(lines)
                        request.write({'custom_purchase_line_id':line.id})

        result = self.env.ref('purchase.purchase_rfq')
        action_ref = result or False
        result = action_ref.sudo().read()[0]
        result['domain'] = str([('id', 'in', rfq_list)])
        return result