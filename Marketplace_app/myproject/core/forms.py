from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Your Password'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Your Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': ' Confirm Password'}))