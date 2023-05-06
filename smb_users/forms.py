from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from .models import Profile

class Registeration_Form(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(Registeration_Form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Re-enter Password'})
        self.order_fields(['username', 'email','password1', 'password2' ])

class Profile_Update_Form(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(Profile_Update_Form, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(initial=self.instance.user.username, disabled= False)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone Number'})
        self.fields['occupation'].widget.attrs.update({'placeholder': 'Occupation'})
        self.fields['image'].widget.attrs.update({'class': 'custom-file-input'})
        self.order_fields(['username', 'email', 'phone', 'occupation', 'image'])
    class Meta:
        model = Profile 
        fields = ['email', 'phone', 'occupation','image']
        
    
