from django.contrib.auth.models import User
from django import forms
from secondapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model= User
        fields=('username','email','password')
class UserProfileInfoform(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
