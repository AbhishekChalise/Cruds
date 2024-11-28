from django import forms
from django.contrib.auth.models import User
from .models import Main_User_Model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Fields from User model

class Main_User_Form(forms.ModelForm):
    class Meta:
        model = Main_User_Model
        fields = ['is_Student', 'is_teacher']  # Fields from Main_User_Model
