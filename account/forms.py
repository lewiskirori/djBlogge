from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise ValidationError("An account with this email address already exists.")
        return email

        
class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    success = None 
    
    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                self.add_error('email', 'Incorrect password. Please try again.')
            else:
                self.success = f"Welcome back!"
        
        return self.cleaned_data
                  
class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        