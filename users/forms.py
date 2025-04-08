from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

# 新增這2個Update Form之後，要到view.py設定
class UserUpdateForm(forms.ModelForm):
    """
    This class allow us to update the username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

class ProfileUpdateForm(forms.ModelForm):
    """
    This class allow us to update profile image.
    """
    class Meta:
        model = Profile
        fields = ['image']
