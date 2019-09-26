from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import GoogleCred, FacebookCred, FacebookFile, GoogleFile

from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'text-center'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class UserGooglePasswordAddForm(forms.ModelForm):

    class Meta:
        model = GoogleCred
        fields = ['google_email_phone', 'google_password']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'text-center'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class UserFacebookPasswordAddForm(forms.ModelForm):

    class Meta:
        model = FacebookCred
        fields = ['facebook_email_phone', 'facebook_password']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'text-center'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class FacebookFileAddForm(forms.ModelForm):
    class Meta:
        model = FacebookFile
        fields = ['path_to_facebook_data', 'availible_stat']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'text-center'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
