from django import forms
from .models import NewUser  
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ["profile_pic","username", "fname","lname", "email","birthday","instagram","twitter","facebook",]
