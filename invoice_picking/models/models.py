from odoo import models,fields,api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit='stock.picking'


    def action_create_invoice(self):
     Sale_order = self.sale_id
    if sale_order.invoice_status == 'invoiced':
        raise UserError("already invoiced")
    return {
        'name':'create invoice',
        'type': 'ir.actions.act_window',
        'res_model' :'invoice.create.wizard',
        'view_mode' : 'form',
        'target': 'new',
        'context' : {
            'default_sale_order_id':  sale_order_id .id,
            'default_ picking_id':  self.id,
        }
    }