from django import forms
from .models import ProfileUser
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ImageField

class AppUserForm(forms.ModelForm):
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AppUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    class Meta:
        model = ProfileUser
        fields = ['username','age','email','gender','blood_type','password']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'age': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'age'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'email'
            }),
            'gender': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'gender'
                }),
            'blood_type': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Blood Group'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
        }





    