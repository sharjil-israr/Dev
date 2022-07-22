from django import forms
from django.forms import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from crispy_forms.bootstrap import InlineRadios
from django.forms import ModelForm, Textarea, TextInput
from driver_engine.models import *
from django.urls import reverse
from django.conf import settings


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'mobile_number', 'blood_group', 'dob', 'education', 'can_read', 'can_write', 'driving_licence_num', 'issuing_authority', 'driving_licence_issue_date', 'driving_licence_expiry_date', 'hgv_licence_issue_date', 'hazard_issue_date', 'address', 'id_card_type', 'card_number', 'bank_ac_holder_name', 'bank_ac_number', 'bank_name', 'ifsc_code', 'joining_date', 'interviewed_by', 'licencse_image', 'hazard_image', 'driver_image', 'created_by')

        widgets = {
            'blood_group' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select Blood Group'}),
            'dob' : forms.DateInput(attrs={'class': 'mt-4', 'type': 'date'}),
            'education' : forms.DateInput(attrs={'class': 'mt-3'}),
            'can_read' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary'}),
            'can_write' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary'}),
            'driving_licence_issue_date' : forms.DateInput(attrs={'type': 'date'}),
            'driving_licence_expiry_date' : forms.DateInput(attrs={'type': 'date'}),
            'hgv_licence_issue_date' : forms.DateInput(attrs={'type': 'date'}),
            'hazard_issue_date' : forms.DateInput(attrs={'type': 'date'}),
            'id_card_type' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select ID Card type'}),
            'joining_date' : forms.DateInput(attrs={'type': 'date'}),
            'status' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select Status'}),
            'created_by' : forms.TextInput(attrs={'type': 'hidden'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['blood_group'].label = ""
        self.fields['can_read'].label = ""
        self.fields['can_write'].label = ""
        self.fields['id_card_type'].label = ""
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_driver', 'Add'))
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('mobile_number'),
            ),
            Row(
                Column('blood_group'),
                Column('dob'),
            ),
            Row(
                Column('education'),
                Column('can_read'),
                Column('can_write'),
            ),
            Row(
                Column('driving_licence_num'),
                Column('issuing_authority'),
            ),
            Row(
                Column('driving_licence_issue_date'),
                Column('driving_licence_expiry_date'),
            ),
            Row(
                Column('hgv_licence_issue_date'),
                Column('hazard_issue_date'),
            ),
            Row(
                Column('address'),
            ),
            Row(
                Column('id_card_type'),
                Column('card_number'),
            ),
            Row(
                Column('bank_ac_holder_name'),
                Column('bank_ac_number'),
            ),
            Row(
                Column('bank_name'),
                Column('ifsc_code'),
            ),
            Row(
                Column('joining_date'),
                Column('interviewed_by'),
                Column('created_by'),
            ),
            Row(
                Column('licencse_image'),
                Column('hazard_image'),
                Column('driver_image'),
        )
    )

class DriverDocumentForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('licencse_image', 'hazard_image', 'driver_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['licencse_image'].label = "Upload Driving License"
        self.fields['hazard_image'].label = "Upload Hazard Card"
        self.fields['driver_image'].label = "Upload Driver's Image"
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_driver', 'Add'))
        self.helper.layout = Layout(
            Row(
                Column('licencse_image'),
                Column('hazard_image'),
                Column('driver_image'),
            ),
        )


class DriverRecruitmentForm(forms.ModelForm):
    class Meta:
        model = DriverRecruitment
        fields = ('driver', 'senior_driver_test_date', 'senior_driver', 'medical_test_date', 'first_aid_date', 'fire_fighting_date', 'company_induction_date', 'ddt_date', 'shell_induction_date', 'created_by')

        widgets = {
            'driver' : forms.TextInput(attrs={'type': 'hidden'}),
            'senior_driver_test_date' : forms.DateInput(attrs={'type': 'date'}),
            'senior_driver' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select Senior Driver'}),
            'medical_test_date' : forms.DateInput(attrs={'type': 'date'}),
            'first_aid_date' : forms.DateInput(attrs={'type': 'date'}),
            'fire_fighting_date' : forms.DateInput(attrs={'type': 'date'}),
            'company_induction_date' : forms.DateInput(attrs={'type': 'date'}),
            'ddt_date' : forms.DateInput(attrs={'type': 'date'}),
            'shell_induction_date' : forms.DateInput(attrs={'type': 'date'}),
            'created_by' : forms.TextInput(attrs={'type': 'hidden'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['senior_driver'].label = ""
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_driver_recruitment_details', 'Add'))
        self.helper.layout = Layout(
            Row(
                Column('senior_driver_test_date'),
                Column('senior_driver'),
            ),
            Row(
                Column('medical_test_date'),
                Column('first_aid_date'),
                Column('fire_fighting_date'),
            ),
            Row(
                Column('company_induction_date'),
                Column('ddt_date'),
                Column('shell_induction_date'),
            ),
            Row(
                Column('driver'),
                Column('created_by'),
        )
    )


class DriverRecruitmentDocumentForm(forms.ModelForm):
    class Meta:
        model = DriverRecruitment
        fields = ('ddt_image', 'shell_induction_image', 'medical_test_image', 'first_aid_image', 'fire_fighting_image', 'company_induction_image')

        widgets = {
            'driver' : forms.TextInput(attrs={'type': 'hidden'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['ddt_image'].label = "Upload DDT Image"
        self.fields['shell_induction_image'].label = "Shell Induction Image"
        self.fields['medical_test_image'].label = "Medical Test Image"
        self.fields['first_aid_image'].label = "First Aid Training Image"
        self.fields['fire_fighting_image'].label = "Fire Fighting Training Image"
        self.fields['company_induction_image'].label = "Company Induction Image"

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_driver_recruitment_document_details', 'Add'))
        self.helper.layout = Layout(
            Row(
                Column('ddt_image'),
                Column('shell_induction_image'),
            ),
            Row(
                Column('medical_test_image'),
                Column('first_aid_image'),
            ),
            Row(
                Column('fire_fighting_image'),
                Column('company_induction_image'),
            ),
            Row(
            Column('driver'),
            ),
        )


class DriverStatusForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('hiring_status','status')

        widgets = {
            'hiring_status' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'Select'}),
            'status' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['hiring_status'].label = "Change Hiring Status"
        self.fields['status'].label = "Change Working Status"

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('change_hiring_status', 'Change Hiring/ working Status'))
        self.helper.layout = Layout(
            Row(
                Column('hiring_status'),
                Column('status'),
            ),
        )



class DriverBehaviourTestForm(forms.ModelForm):
    class Meta:
        model = DriverBehaviourTest
        fields = ('driver', 'q1a', 'q1b', 'q1c', 'q1d', 'q2a', 'q2b', 'q2c', 'q2d', 'q3a', 'q3b', 'q3c', 'q3d', 'q4a', 'q4b', 'q4c', 'q4d', 'q5a', 'q5b', 'q5c', 'q5d', 'created_by')

        widgets = {
            'driver' : forms.TextInput(attrs={'type': 'hidden'}),
            'q1a' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q1b' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q1c' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q1d' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),

            'q2a' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q2b' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q2c' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q2d' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),

            'q3a' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q3b' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q3c' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q3d' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),

            'q4a' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q4b' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q4c' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q4d' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),

            'q5a' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q5b' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q5c' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'q5d' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn btn-primary', 'title': 'select'}),

            'created_by' : forms.TextInput(attrs={'type': 'hidden'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1a'].label = "I make friends easily"
        self.fields['q1b'].label = "I trust others"
        self.fields['q1c'].label = "I complete tasks successfully"
        self.fields['q1d'].label = "I get tensed easily"

        self.fields['q2a'].label = "I get angry easily"
        self.fields['q2b'].label = "I use and manipulate others to get my way"
        self.fields['q2c'].label = "I am a tidy person"
        self.fields['q2d'].label = "I enjoy company"
        
        self.fields['q3a'].label = "I always feel cheerful"
        self.fields['q3b'].label = "I like to take charge of situation"
        self.fields['q3c'].label = "I like to help others"
        self.fields['q3d'].label = "I keep my promises"

        self.fields['q4a'].label = "I love excitement"
        self.fields['q4b'].label = "I enjoy challenges"
        self.fields['q4c'].label = "I am always prepared"
        self.fields['q4d'].label = "I take immediate decisions"

        self.fields['q5a'].label = "I love to drive"
        self.fields['q5b'].label = "I love life"
        self.fields['q5c'].label = "I don't like to breaking rules"
        self.fields['q5d'].label = "I satisfied with my income"

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_driver_behaviour_test', 'Add behaviour test'))
        self.helper.layout = Layout(
            Row(
                Column('q1a'),
            ),
            Row(
                Column('q1b'),
            ),
            Row(
                Column('q1c'),
            ),
            Row(
                Column('q1d'),
            ),
            Row(
                Column('q2a'),
            ),
            Row(
                Column('q2b'),
            ),
            Row(
                Column('q2c'),
            ),
            Row(
                Column('q2d'),
            ),
            Row(
                Column('q3a'),
            ),
            Row(
                Column('q3b'),
            ),
            Row(
                Column('q3c'),
            ),
            Row(
                Column('q3d'),
            ),
            Row(
                Column('q4a'),
            ),
            Row(
                Column('q4b'),
            ),
            Row(
                Column('q4c'),
            ),
            Row(
                Column('q4d'),
            ),
            Row(
                Column('q5a'),
            ),
            Row(
                Column('q5b'),
            ),
            Row(
                Column('q5c'),
            ),
            Row(
                Column('q5d'),
            ),
            Row(
                Column('driver'),
                Column('created_by'),
        )
    )


class DriverLeaveForm(forms.ModelForm):
    class Meta:
        model = DriverLeave
        fields = ('driver','from_date', 'to_date', 'reason', 'created_by')

        widgets = {
            'driver' : forms.Select(attrs={'class': 'selectpicker mb-5', 'data-style': 'btn btn-primary', 'title': 'select'}),
            'from_date' : forms.DateInput(attrs={'type': 'date'}),
            'to_date' : forms.DateInput(attrs={'type': 'date'}),
            'created_by' : forms.TextInput(attrs={'type': 'hidden'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['from_date'].label = "Leave From Date"
        self.fields['to_date'].label = "Leave To Date"
        self.fields['reason'].label = "Leave Reason"

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_leave_driver', 'Add'))
        self.helper.layout = Layout(
            Row(
                Column('driver'),
                Column(),
            ),
            Row(
                Column('from_date'),
                Column('to_date'),
            ),
            Row(
                Column('reason'),
                Column(),
            ),
            Row(
                Column('created_by'),
            )
        )
