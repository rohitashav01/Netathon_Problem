from django import forms
from .models import AppUser


class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['name','age','email','gender','blood_type','password']

    