# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CitizenUser, StaffUser
from django.forms import ModelForm

class CitizenUserCreationForm(UserCreationForm):
    class Meta:
        model = CitizenUser
        fields = ['name','phone','email','username','password1','password2']

class StaffUserCreationForm(UserCreationForm):
    class Meta:
        model = StaffUser
        fields = ['name','phone','email','position','village_code','username','password1','password2']




