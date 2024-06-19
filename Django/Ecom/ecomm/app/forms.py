from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'required': 'True',
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': 'True',
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'True',
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'True',
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'required': 'True',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
