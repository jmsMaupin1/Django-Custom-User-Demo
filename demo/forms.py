from django import forms
from django.contrib.auth.forms import UserCreationForm

from custom_user.models import MyCustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = MyCustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'favorite_color'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)