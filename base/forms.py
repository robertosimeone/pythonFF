from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required')
    username = forms.CharField(max_length=30,help_text = 'Required')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists.')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username