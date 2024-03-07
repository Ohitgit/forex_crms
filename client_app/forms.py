# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))





class ForgotForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class':'form-control'}))
    


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password','class':'form-control'}))
    confrimpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confrimpassword','class':'form-control'}))
