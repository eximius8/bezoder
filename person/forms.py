from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile
from captcha.fields import ReCaptchaField
User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
