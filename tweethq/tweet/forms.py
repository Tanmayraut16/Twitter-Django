from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']  # Replace 'tweet' with 'text'


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Add email field
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Add 'email' to the list of fields