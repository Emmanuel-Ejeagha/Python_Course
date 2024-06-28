from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'autofocus': 'True',
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
            'placeholder': 'Password',
            'class': 'form-control',
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

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class':'form-control'}),
        }
