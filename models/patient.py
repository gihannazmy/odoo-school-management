from dateutil.relativedelta import relativedelta

from odoo import models,fields, api



class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"
    _rec_name = 'display_name'
    display_name = fields.Char(
        string='Full Name',
        compute='_compute_display_name',
        store=True
    )
    first_name = fields.Char(string="First Name", required='True')
    last_name = fields.Char(string="Last Name", required='True')
    birth_date = fields.Date(string="Birth Date")
    history = fields.Html()
    cr_ratio = fields.Float()
    pcr = fields.Boolean()

    blood_type = fields.Selection(
        string="Blood Type",
        selection=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]
    )
    profile_image = fields.Image()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age')
    state = fields.Selection([
        ('undetermined','Undetermined'),
        ('good','Good'),
        ('fair','Fair'),
        ('serious','Serious')],
    default='undetermined')
    email = fields.Char( unique=True)

    department_id = fields.Many2one(
    'hms.department',
    string="Department"
)
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors', domain="[('department_id', '=', department_id)]")
    department_capacity = fields.Integer(
        related='department_id.capacity',
        readonly=True
    )
    patient_log_ids = fields.One2many('hms.patient.log', 'patient_id')

    def action_undetermined(self):
        self.state ='undetermined'

    def action_good(self):
        self.state ='good'

    def action_fair(self):
        self.state ='fair'

    def action_serious(self):
        self.state ='serious'

    def action_add_log_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('hospital_management_system.add_log_action_view')
        action['context'] = {
            'default_patient_id':self.id
        }
        return action

  # Points to the computed field

    @api.depends('first_name', 'last_name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.first_name} {record.last_name}"

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta(fields.Date.today(),rec.birth_date).years
            else:
                rec.age = 0

    @api.onchange('department_id')
    def _onchange_department(self):
        if self.department_id:
            return {
                'domain': {
                    'doctor_ids': [('department_id', '=', self.department_id.id)]
                },
                'warning': {
                    'title': "Notice",
                    'message': "You can now select doctors from this department"
                }
            }
        else:
            self.doctor_ids = False
            return {
                'domain': {
                    'doctor_ids': [('id', 'in', [])]
                }
            }
    @api.onchange('age')
    def _onchange_age(self):
        for rec in self:
            if rec.age and rec.age > 30:
                rec.pcr = True
                return {
                    'warning': {
                        'title': ("PCR Auto-Checked"),
                        'message':("PCR has been automatically checked because the patient is under 30 years old."),
                    }
                }

class PatientLog(models.Model):
    _name = "hms.patient.log"
    _description = 'Patient Log'

    date = fields.Date(default=fields.Date.today())
    description = fields.Text()
    created_by = fields.Many2one(
        'res.users',
        string="Created By",
        default=lambda self: self.env.user
    )
    patient_id = fields.Many2one('hms.patient')