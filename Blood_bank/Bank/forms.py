from django import forms
from .models import ProfileUser,Diseases, Chat
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput,Select,CheckboxInput

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
        fields = ['username','age','email','gender','blood_type','password','is_donor']
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
            'gender': Select(attrs={
                'class': "form-control",
                'placeholder': 'gender'
                }),
            'blood_type': Select(attrs={
                'class': "form-control",
                'placeholder': 'Blood Group'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
            'is_donor': CheckboxInput(attrs={
                'class': "form-check",
            }),
        }


class DiseaseForm(forms.ModelForm):
        class Meta:
            model = Diseases
            fields = ['aids','asthma','bleeding_disorder','cancer','heart_disease','hepatitis_b_or_c','mad_cow']
            widgets = {
                'aids': CheckboxInput(attrs={
                    'class': "form-check",
                    }),
                'asthma': CheckboxInput(attrs={
                    'class': "form-check",
                    }),
                'bleeding_disorder': CheckboxInput(attrs={
                    'class': "form-check",
                }),
                'cancer': CheckboxInput(attrs={
                    'class': "form-check",
                    }),
                'heart_disease': CheckboxInput(attrs={
                    'class': "form-check",
                    }),
                'hepatitis_b_or_c':CheckboxInput(attrs={
                    'class': "form-check",
                    }),
                'mad_cow': CheckboxInput(attrs={
                    'class': "form-check",
                }),
            }


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']

    