from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class signupform(forms.Form):
	username=forms.CharField(label='Username',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':'username','placeholder':'Username'}))
	email=forms.EmailField(label='Email',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':'email','placeholder':'E-mail'}))
	password1 = forms.CharField(label="Password", max_length=30, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Password'})))
	password2 = forms.CharField(label="Password(again)", max_length=30, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password(again)','placeholder':'Confirm Password'})))
    