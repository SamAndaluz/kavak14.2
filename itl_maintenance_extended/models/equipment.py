from odoo import api, fields, models, tools
from odoo.osv import expression


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    # https://itlglobaltech.odoo.com/web#id=2930&menu_id=504&cids=1&action=700&model=project.task&view_type=form
    barcode = fields.Char(help="Use a barcode to identify this Equipment.", copy=False, company_dependent=True)

    @api.constrains('barcode')
    def _check_barcode(self):
        """
        Use: Barcode must be unique
        Added by: Jignesh
        Added on: 22/4/22
        Task: https://itlglobaltech.odoo.com/web#id=2930&menu_id=504&cids=1&action=700&model=project.task&view_type=form
        """
        for equipment in self.filtered(lambda p: p.barcode):
            existing_equipment = self.search([('id', '!=', equipment.id), ('barcode', '=', equipment.barcode)])
            if existing_equipment:
                raise Warning("You can't have the same Barcode in Equipment twice!")

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        Use: Equipment search by Barcode also
        Added by: Jignesh
        Added on: 22/4/22
        Task: https://itlglobaltech.odoo.com/web#id=2930&menu_id=504&cids=1&action=700&model=project.task&view_type=form
        """
        domain = expression.AND([args or [], ['|',
                                              ('name', operator, name),
                                              ('barcode', operator, name),
                                              ]])
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)
