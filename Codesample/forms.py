from urllib3 import fields
import imghdr

from django.core import validators
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from models import Fotos, UserModel
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['email','password']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model= UserModel
        fields='__all__'
    def clean_username(self):
        try:
            user = UserModel.objects.get(username__iexact=self.cleaned_data['username'])
        except UserModel.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean_password(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data


class FotosForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = '__all__'

    def isImage(self):
        if imghdr.what(self.foto) == 'jpg' or imghdr.what(self.foto) == 'jpeg' or imghdr.what(
                self.foto) == 'png' or imghdr.what(self.foto) == 'gif':
            return True
        else:
            return False
