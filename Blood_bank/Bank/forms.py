from django import forms
from .models import ProfileUser


class AppUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['username','age','email','gender','blood_type']

    