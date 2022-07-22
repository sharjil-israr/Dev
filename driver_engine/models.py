import datetime
from datetime import date, timedelta
from dateutil import relativedelta
from django.db import models
from accounts_engine.models import *

class Driver(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=10)

    BLOOD_GROUP_LIST = [
    ('', 'Select Blood Group'),    
    ('0', 'O +ve'),
    ('1', 'O -ve'),
    ('2', 'A +ve'),
    ('3', 'A -ve'),
    ('4', 'B +ve'),
    ('5', 'B -ve'),
    ('6', 'AB +ve'),
    ('7', 'AB -ve'),
    ]

    blood_group = models.CharField(max_length = 100,choices = BLOOD_GROUP_LIST)
    dob = models.DateField()
    education = models.CharField(max_length=200)
    
    CAN_READ_LIST = [
    ('', 'CAN READ?'),
    (True, 'Yes'),
    (False, 'No'),
    ]
    
    can_read = models.BooleanField(choices = CAN_READ_LIST)

    CAN_WRITE_LIST = [
    ('', 'CAN WRITE?'),
    (True, 'Yes'),
    (False, 'No'),
    ]

    can_write = models.BooleanField(choices = CAN_WRITE_LIST)
    driving_licence_num = models.CharField(max_length=16)
    issuing_authority = models.CharField(max_length=200)
    driving_licence_issue_date = models.DateField()
    driving_licence_expiry_date = models.DateField()
    hgv_licence_issue_date = models.DateField()
    hazard_issue_date = models.DateField()
    address = models.TextField()

    IDENTITY_PROOF_LIST = [
    ('aadhar card', 'Aadhar Card'),
    ('Election Card', 'Election Card'),
    ('passport', 'Passport'),
    ('driving licencse', 'Driving Licencse'),
    ]

    id_card_type = models.CharField(max_length = 100,choices = IDENTITY_PROOF_LIST, default='aadhar card')
    card_number = models.CharField(max_length=200)

    bank_ac_holder_name = models.CharField(max_length=200)
    bank_ac_number = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=200)

    joining_date = models.DateField()
    interviewed_by = models.CharField(max_length=200)

    STATUS_LIST = [
        ('0', 'In Active'),
        ('1', 'Active'),
    ]

    status = models.CharField(max_length = 10,choices = STATUS_LIST, default='0')

    HIRING_LIST = [
        ('0', 'In process'),
        ('1', 'On Hold'),
        ('2', 'Selected'),
        ('3', 'Rejected'),
    ]

    hiring_status = models.CharField(max_length = 10,choices = HIRING_LIST, default='0')

    LEAVE_LIST = [
    ('', 'ON LEAVE'),
    (True, 'Yes'),
    (False, 'No'),
    ]

    on_leave = models.BooleanField(choices = LEAVE_LIST)

    licencse_image = models.ImageField(upload_to='media/dl/', null=True, blank=True)
    hazard_image = models.ImageField(upload_to='media/hazard/', null=True, blank=True)
    driver_image = models.ImageField(upload_to='media/profile_pic/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


    def age(self):
        today = datetime.date.today()
        dob = self.dob
        years = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            years -= 1
        return years

    def age_in_company(self):
        today = datetime.date.today()
        # years = today.year - self.joining_date.year
        # if today.month < self.joining_date.month or (today.month == self.joining_date.month and today.day < self.joining_date.day):
        #     years -= 1
        r = relativedelta.relativedelta(today, self.joining_date)
        return_string = str(r.years) + ' years, ' + str(r.months) + ' months'
        return return_string

    def get_senior_junior(self):
        today = datetime.date.today()
        r = relativedelta.relativedelta(today, self.joining_date)
        total_months = r.years * 12 + r.months
        if total_months > 6:
            return {'senior_or_junior': 'Senior', 'colour': 'success'}
        else:
            return {'senior_or_junior': 'Junior', 'colour': 'warning'}

    def get_senior_junior(self):
        today = datetime.date.today()
        r = relativedelta.relativedelta(today, self.joining_date)
        total_months = r.years * 12 + r.months
        if total_months > 6:
            return {'senior_or_junior': 'Senior', 'colour': 'success'}
        else:
            return {'senior_or_junior': 'Junior', 'colour': 'warning'}

    def get_status_colour(self):
        if self.status == '0':
            return 'danger'
        if self.status == '1':
            return 'success'
        if self.status == '2':
            return 'warning'

    def get_license_status(self):
        today = datetime.date.today()
        r = relativedelta.relativedelta(self.driving_licence_expiry_date, today)
        total_months = r.years * 12 + r.months
        if total_months < 0:
            return {'status': 'License expired', 'colour': 'danger'}
        if total_months == 1:
            return {'status': 'License expiring', 'colour': 'warning'}
        else:
            return {'status': 'License Valid', 'colour': 'success'}

    def get_hazard_expiry_status(self):
        today = datetime.date.today()
        hazard_expiry_date = self.hazard_issue_date + timedelta(days=365)
        r = relativedelta.relativedelta(hazard_expiry_date, today)
        total_months = r.years * 12 + r.months
        if total_months < 0:
            return {'status': 'Hazard expired', 'colour': 'danger'}
        if total_months == 1:
            return {'status': 'Hazard expiring', 'colour': 'warning'}
        else:
            return {'status': 'Hazard Valid', 'colour': 'success'}

    def get_hiring_status(self):
        status = ['Recruitment Done'] 
        try:
            behaviour_test = DriverBehaviourTest.objects.get(driver = self)
            status.append('Behaviour Test Done')
        except:
            pass 
        return status
        

    

class DriverBehaviourTest(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='drivers_behaviour')
    ANSWER_LIST = [
        ('', 'SELECT'),
        ('5', 'Agree'),
        ('3', 'Neutral'),
        ('1', 'Disagree'),
    ]
    q1a = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q1b = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q1c = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q1d = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q2a = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q2b = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q2c = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q2d = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q3a = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q3b = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q3c = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q3d = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q4a = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q4b = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q4c = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q4d = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q5a = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q5b = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q5c = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')
    q5d = models.CharField(max_length = 10,choices = ANSWER_LIST, default='')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_behaviour_question_and_answer(self):
        from driver_engine.forms import DriverBehaviourTestForm
        form = DriverBehaviourTestForm()
        qna_list = []
        for field in form:
            temp_dict = {}
            temp_dict['field'] = field.name
            temp_dict['q'] = field.label
            temp_dict['a'] = getattr(self, field.name)
            if not field.name == 'driver':
                qna_list.append(temp_dict)
        
        return qna_list

    def get_total_marks(self):
        total = 0
        total = int(self.q1a) + int(self.q1b) + int(self.q1c) + int(self.q1d)
        total += int(self.q2a) + int(self.q2b) + int(self.q2c) + int(self.q2d)
        total += int(self.q3a) + int(self.q3b) + int(self.q3c) + int(self.q3d)
        total += int(self.q4a) + int(self.q4b) + int(self.q4c) + int(self.q4d)
        return total

    def get_result(self):
        total = self.get_total_marks()
        if total >= 60:
            return 'can be hired'
        if total < 60 and total >= 30:
            return 'needs to be trained'
        if total < 30:
            return 'cannot be hired'


class DriverRecruitment(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='drivers')

    past_experience = models.TextField(null=True, blank=True)
    past_experience_verified = models.BooleanField(default=False)
    
    senior_driver_test = models.TextField(null=True, blank=True)
    senior_driver_test_date = models.DateField(null=True, blank=True)
    senior_driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='senior_drivers', null=True, blank=True)

    ddt_date = models.DateField(null=True, blank=True)
    ddt_image = models.ImageField(upload_to='media/ddt/', null=True, blank=True)
    
    GRADE_LIST = [
        ('', 'SELECT'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    ddt_grade = models.CharField(max_length = 10,choices = GRADE_LIST, default='', null=True, blank=True)

    induction_date = models.DateTimeField(null=True, blank=True) 
    induction_image = models.ImageField(upload_to='media/induction/', null=True, blank=True)

    medical_test_date = models.DateField(null=True, blank=True)
    first_aid_date = models.DateField(null=True, blank=True)
    fire_fighting_date = models.DateField(null=True, blank=True)
    company_induction_date = models.DateField(null=True, blank=True)
    
    shell_induction_date = models.DateTimeField(null=True, blank=True)
    shell_induction_image = models.ImageField(upload_to='media/shell_induction/', null=True, blank=True)
    medical_test_image = models.ImageField(upload_to='media/medical/', null=True, blank=True)
    first_aid_image = models.ImageField(upload_to='media/first_aid/', null=True, blank=True)
    fire_fighting_image = models.ImageField(upload_to='media/fire_fighting/', null=True, blank=True)
    company_induction_image = models.ImageField(upload_to='media/company_induction/', null=True, blank=True)

    shell_id = models.CharField(max_length = 10, null=True, blank=True)
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class DriverLeave(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length = 200)

    STATUS_LIST = [
        ('0', 'Not Reviewed'),
        ('1', 'Accepted'),
        ('2', 'Rejected'),
    ]

    status = models.CharField(max_length = 20, choices = STATUS_LIST, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
