from django import forms
from .models import RegistrationData

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter username'
                                }))
    password = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter password'
                                }))
    email = forms.CharField(max_length=100,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Email'
                                }))
    phone = forms.CharField(max_length=100,
                                widget=forms.NumberInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Phone'
                                }))


class RegistrationModal(forms.ModelForm):
    class Meta:

        model = RegistrationData

        fields = [
            'username',
            'password',
            'email',
            'phone'
        ]

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),

            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone'
            })

        }
