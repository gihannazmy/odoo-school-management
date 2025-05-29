from  odoo import fields, models




class AddLog(models.TransientModel):

    _name = 'hms.add.log'
    _description = "Patient Log"

    patient_id = fields.Many2one('hms.patient', required=True)
    description = fields.Text()


    def action_add_log(self):
        self.ensure_one()

        self.book_id.publisher_id = self.publisher_id.id
