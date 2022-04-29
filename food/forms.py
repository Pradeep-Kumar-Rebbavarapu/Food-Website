from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import *
            

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        help_texts = {
            'email':'Required',
            'first_name':'Required',
            'last_name':'Required'
        }
        widgets = {
            'username':forms.TextInput(attrs ={
                'id':'message'
            }),

            'password':forms.PasswordInput(attrs ={
                'id':'message'
            } ),

            'email':forms.EmailInput(attrs = {
                'id':'message'
            }),

            'first_name':forms.TextInput(attrs = {
                'id':'message'
            }),

            'last_name':forms.TextInput(attrs = {
                'id':'message'
            }),
        }

class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'message'}))
