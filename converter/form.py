from django import forms  
from .models import Image
from django.contrib.auth.models import User

class Uploadform(forms.Form):  
    file   = forms.FileField() # for creating file input  

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["imagefile1","imagefile2","imagefile3","imagefile4","imagefile5","imagefile6"]
        exclude = ['user_name']
