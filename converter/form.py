from django import forms  
from .models import Image


class Uploadform(forms.Form):  
    file   = forms.FileField() # for creating file input  

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
