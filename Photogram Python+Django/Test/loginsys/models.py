from django.db import models
from django import forms


class RegForm(forms.Form):
    username = forms.CharField(max_length = 15)
    password = forms.CharField(widget = forms.PasswordInput(), max_length=30)
    repeat_password = forms.CharField(widget = forms.PasswordInput(), max_length=30)



