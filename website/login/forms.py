from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email', 'zip_code']


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']