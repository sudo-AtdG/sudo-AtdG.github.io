from .models import Contacts
from django.forms import ModelForm, TextInput, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone', 'email']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
        }