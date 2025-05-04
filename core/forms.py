from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from .models import Group, UserProfile
User = get_user_model()
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio',  'github_url', 'preferred_language']

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
