from django import forms


class PasswordForm(forms.Form):
    password = forms.CharField()


class UsernameForm(forms.Form):
    username = forms.CharField(min_length=3)
