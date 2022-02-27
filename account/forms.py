from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email']
        widgets = {
        'first_name': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'First Name'
            }),
        'last_name': TextInput(attrs={
            'class': "form-control", 
            'placeholder': 'Last Name'
            }),
        'email': EmailInput(attrs={
            'class': "form-control", 
            'placeholder': 'Your Email'
            })
        }