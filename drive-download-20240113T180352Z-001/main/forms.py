from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"type_here", "placeholder": "gmail@gmail.com"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"type_here", "placeholder": "Your_Username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"type_here", "placeholder": "Select Password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"type_here", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

