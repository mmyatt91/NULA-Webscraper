from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import SelectField

class ResourceMenuForm(FlaskForm):
    """Form for choosing a resource from 
    dropdown menu"""

    resource = SelectField(
        "Choose a Resource",
        choices =[
            (0, 'Select A Resource'),
            (1, 'Crisis Support, Helplines & Warmlines'),
            (2, 'Organizations & Campaigns'),
            (3, 'Mental Health, Rehab & Counseling Services'),
            (4, 'Psychiatric Inpatient Services'),
            (5, 'Outpatient Clinics & Wellness Centers'),
            (6, 'Urgent Care Centers'),
            (7, 'Support Groups & Education Classes'),
            (8, 'Transitional Age Youth Drop-In Centers & Services'),
            (9, 'Benefits Assistance, Housing, Shelters & Food'),
            (10, 'Peer Centers & Respites'),
            (11, 'Apps'),
            (12, 'Holistic Health')]
    )


    #CATEGORIES
    CATEGORIES = {
        1: 'Crisis Support, Helplines & Warmlines',
        2: 'Organizations & Campaigns',
        3: 'Mental Health, Rehab & Counseling Services',
        4: 'Psychiatric Inpatient Services',
        5: 'Outpatient Clinics & Wellness Centers',
        6: 'Urgent Care Centers',
        7: 'Support Groups & Education Classes',
        8: 'Transitional Age Youth Drop-In Centers & Services',
        9: 'Benefits Assistance, Housing, Shelters & Food',
        10: 'Peer Centers & Respites',
        11: 'Apps',
        12: 'Holistic Health'
    }


[<u>CRISIS SUPPORT, HELPLINES &amp; WARMLINES</u>,
 <u>ORGANIZATIONS &amp; CAMPAIGNS</u>,
 <u>MENTAL HEALTH, REHAB, &amp; COUNSELING SERVICES</u>,
 <u>PSYCHIATRIC INPATIENT SERVICES</u>,
 <u>OUTPATIENT CLINICS &amp; WELLNESS CENTERS</u>,
 <u>URGENT CARE CENTERS</u>,
 <u>SUPPORT GROUPS &amp; EDUCATION CLASSES</u>,
 <u>TRANSITIONAL AGE YOUTH DROP-IN CENTERS/SERVICES</u>,
 <u>BENEFITS ASSISTANCE, HOUSING, SHELTERS &amp; FOOD</u>,
 <u>PEER CENTERS &amp; RESPITES</u>,
 <u>APPS</u>,
 <u>HOLISTIC HEALTH</u>]

'<strong>National Suicide Prevention Lifeline</strong> <a href="http://www.suicidepreventionlifeline.org" target="_blank">www.suicidepreventionlifeline.org</a>
\n<strong>National Hopeline Network</strong> <a href="http://www.hopeline.com" target="_blank">www.hopeline.com</a>
\n<strong>NAMI National\'s Helpline</strong> <a href="mailto:info@nami.org">info@nami.org </a>
\n<strong>Crisis Text Line</strong> <a href="https://www.nami.org/Find-Support/NAMI-HelpLine" target="_blank">https://www.nami.org</a>
\n<strong>Panic Disorder Info Hotline</strong> <a href="https://www.crisistextline.org" target="_blank">www.CrisisTextLine.org</a>
\n<strong>Teen Line</strong> <a href="http://www.TeenLineOnline.org" target="_blank">www.TeenLineOnline.org</a>
\n<strong>CA Youth Crisis Line</strong> <a href="https://calyouth.org" target="_blank">https://calyouth.org</a>
\n<strong>The Trevor Project</strong> <a href="http://www.TheTrevorProject.org" target="_blank">www.TheTrevorProject.org</a>
\n<strong>Trans Lifeline</strong> <a href="https://www.translifeline.org" target="_blank">https://www.translifeline.org</a>
\n<strong>ACCESS-LA County Helpline</strong> <a href="http://dmh.lacounty.gov/" target="_blank">dmh.lacounty.gov</a>\n<strong>2-1-1</strong> <a href="http://www.211.org" target="_blank">http://www.211.org</a>
\n<strong>7 Cups Of Tea</strong> <a href="https://www.7cups.com" target="_blank">www.7cups.com</a>
\n<strong>Project Return Warm Line</strong> <a href="http://prpsn.org/services/warm-line" target="_blank">http://prpsn.org/services/warm-line</a>
\n<strong>LA Warmline</strong> <a href="https://www.nationaleatingdisorders.org" target="_blank">www.nationaleatingdisorders.org</a>
\n<strong><span class="s-text-color-black">NEDA Helpline</span></strong> <a href="https://www.veteranscrisisline.net" target="_blank">https://www.veteranscrisisline.net</a>
\n<strong>Veterans Crisis Line</strong> <a href="https://www.samhsa.gov/find-help/national-helpline" target="_blank">www.samhsa.gov/find-help/national-helpline</a>
\n<strong>SAMHSA National Helpline</strong> <a href="https://addictionresource.com" target="_blank">https://addictionresource.com</a>
\n<strong>Addiction Resource Rehab Helpline</strong> <a href="https://www.samhsa.gov/find-help/disaster-distress-helpline" target="_blank">www.disasterdistress.samhsa.gov</a>
\n<strong>Disaster Distress Helpline</strong> <a href="https://www.thehotline.org" target="_blank">https://www.thehotline.org</a>
\n<strong>National Domestic Violence Hotline</strong> <a href="https://www.rainn.org" target="_blank">https://www.rainn.org</a>'