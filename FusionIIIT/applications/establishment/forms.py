from django import forms
from .models import Constants

dec = 'I hereby declare that I have uploaded & updated all my achievements (including publications, visits, projects etc.) on Institute\'s website and EIS module.'
dec2 = 'I hereby declare that the family members for whom the L.T.C. is claimed are residing with me and are wholly dependent upon me.'
dec3 = 'I hereby declare that the previous LTC advance drawn by me has already been adjusted.'

class Cpda_Form(forms.Form):
    pf_number = forms.CharField(label='PF Number', required=True)
    purpose = forms.CharField(label='Purpose', widget=forms.TextInput, required=True)
    requested_advance = forms.IntegerField(label='Advance Requested', min_value=0, required=True)
    declaration = forms.BooleanField(label=dec, required=True)

    
class Cpda_Bills_Form(forms.Form):
    app_id = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    adjustment_amount = forms.IntegerField(label='Adjustment Amount', min_value=0, required=True)
    bills = forms.FileField(label='Bills')
    total_bills_amount = forms.IntegerField(label='Total Bills Amount', min_value=0, required=True)


class Ltc_Form(forms.Form):
    pf_number = forms.CharField(label='PF Number', required=True)
    basic_pay = forms.IntegerField(label='Basic Pay', min_value=0, required=True)

    is_leave_req = forms.ChoiceField(label='Is leave required ?', choices=Constants.LTC_LEAVE, required=True)
    leave_start = forms.DateField(label='Leave Start Date')
    leave_end = forms.DateField(label='Leave End Date')
    family_departure_date = forms.DateField(label='Family Departure Date')
    leave_nature = forms.CharField(label='Leave Nature')
    purpose = forms.CharField(label='Purpose', widget=forms.TextInput, required=True)
    leave_type = forms.ChoiceField(label='Whether L.T.C. is desired for going to home town or elsewhere?', choices=Constants.LTC_TYPE)
    address_during_leave = forms.CharField(label='Address During Leave', widget=forms.TextInput)
    phone_number = forms.CharField(label='Phone Number', required=True)
    travel_mode = forms.ChoiceField(label='Mode of Travel', choices=Constants.LTC_TRAVEL, required=True)
    
    ltc_availed = forms.CharField(label='Details of family members that have already availed LTC in this block', widget=forms.TextInput, required=True)
    ltc_to_avail = forms.CharField(label='Details of family members who will avail LTC: Name, Age', widget=forms.TextInput, required=True)
    dependents = forms.CharField(label='Details of all dependents: Name, Age, Why fully dependent?', widget=forms.TextInput, required=True)

    requested_advance = forms.IntegerField(label='Advance Requested', min_value=0, required=True)
    declaration = forms.BooleanField(label=dec2, required=True)
    declaration2 = forms.BooleanField(label=dec3, required=True)


class Assign_Form(forms.Form):
    app_id = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    status = forms.ChoiceField(choices=Constants.STATUS)
    reviewer_id = forms.CharField(label="Reviewer ID", required=False)
    reviewer_design = forms.CharField(label="Reviewer Designation", required=False)
    remarks = forms.CharField(label="Remarks")


class Review_Form(forms.Form):
    app_id = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    remarks = forms.CharField(label="Remarks", required=True)


class Ltc_Eligible_Form(forms.Form):
    username = forms.CharField(label="Username", required=True)
    joining_date = forms.DateField(label='Employee Joining Date', required=True)
    current_block_size = forms.IntegerField(label="Current LTC Block Size", required=True, min_value=0)

    total_ltc_allowed = forms.IntegerField(label="Total LTC allowed", min_value=0)
    hometown_ltc_allowed = forms.IntegerField(label="Hometown LTC allowed", min_value=0)
    elsewhere_ltc_allowed = forms.IntegerField(label="Elsewhere LTC allowed", min_value=0)

    hometown_ltc_availed = forms.IntegerField(label="Hometown LTC availed", min_value=0)
    elsewhere_ltc_availed = forms.IntegerField(label="Elsewhere LTC availed", min_value=0)
