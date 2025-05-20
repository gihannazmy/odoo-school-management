from odoo import models,fields


class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"

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
    age = fields.Integer()
    state = fields.Selection([
        ('undetermined','Undetermined'),
        ('good','Good'),
        ('fair','Fair'),
        ('serious','Serious')],
    default='undetermined')


    department_id = fields.Many2one(
    'hms.department',
    string="Departments"
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


class PatientLog(models.Model):
    _name = "hms.patient.log"
    _description = 'Patient Log'

    date = fields.Date()
    description = fields.Text()
    created_by = fields.Many2one(
        'res.users',
        string="Created By",
        default=lambda self: self.env.user
    )
    patient_id = fields.Many2one('hms.patient')