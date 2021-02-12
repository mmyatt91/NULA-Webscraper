from flask_wtf import FlaskForm
from wtforms import SelectField

CATEGORIES = [
            (0, 'Crisis Support, Helplines & Warmlines'),
            (1, 'Organizations & Campaigns'),
            (2, 'Mental Health, Rehab & Counseling Services'),
            (3, 'Psychiatric Inpatient Services'),
            (4, 'Outpatient Clinics & Wellness Centers'),
            (5, 'Urgent Care Centers'),
            (6, 'Support Groups & Education Classes'),
            (7, 'Transitional Age Youth Drop-In Centers & Services'),
            (8, 'Benefits Assistance, Housing, Shelters & Food'),
            (9, 'Peer Centers & Respites'),
            (10, 'Apps'),
            (11, 'Holistic Health')]

class ResourceMenuForm(FlaskForm):
    """Form for choosing a resource from 
    dropdown menu"""

    resource = SelectField("Select A Resource:", choices = CATEGORIES)