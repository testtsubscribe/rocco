from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactInquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your Name')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your Email')
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your Phone Number')
            }),
            'service': forms.Select(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Your Message'),
                'rows': 5
            }),
        }
        labels = {
            'name': _('Full Name'),
            'email': _('Email Address'),
            'phone': _('Phone Number'),
            'service': _('Service Interested In'),
            'message': _('Your Message'),
        }