from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    

    po_approval_category_id = fields.Many2one(related="company_id.po_approval_category_id", string="Categoría de Aprobación", help="Categoría de aprobación usada cuando una compra se manda a aprobación.", readonly=False)