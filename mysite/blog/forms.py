
from cProfile import label
from dataclasses import field
from pyexpat import model
from django import forms
# from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 

from .models import Post,Comments,UserImage


class UserSignupForm(UserCreationForm):
    password2= forms.CharField(label='Confirm password' , widget=forms.PasswordInput)
    class Meta:
        model= User 

        fields =['username' ,'first_name' , 'last_name' ,'email' ]
        labels = {'email':'Email' , 'first_name':'First Name', 'last_name':'Last Name'}

class UserUpdateForm(UserChangeForm):
    password= None

    class Meta:
        model= User
        fields = ['username' , 'first_name' , 'last_name' , 'email']

class UserPostForm(forms.ModelForm):
    content= forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Post
        fields= ['title' ,'image' , 'exerpt' , 'content'  ,'tag' ]

class UserCommentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']
    
class userImageForm(forms.ModelForm):
  
    youtube = forms.URLField(required=False ,label='YouTube Channel')
    twiter = forms.URLField(required=False ,label='Twitter Id')
    instagram = forms.URLField(required=False ,label='Insatgram Id' )
    class Meta:
        model= UserImage
        fields = ['uimage','aboutme','designation','youtube','twiter','instagram']
        # required_fields =['aboutme','designation']
        labels= {
            'uimage':"User Image", 'aboutme':'About Me','designation':'Designation',
            
        }