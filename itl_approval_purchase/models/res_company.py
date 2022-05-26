from odoo import fields, models

class Company(models.Model):
    _inherit = 'res.company'
    
    po_approval_category_id = fields.Many2one('approval.category', string="Categoría de Aprobación", help="Categoría de aprobación usada cuando una compra se manda a aprobación.")