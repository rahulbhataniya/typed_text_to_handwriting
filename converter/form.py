from django import forms  
class Uploadform(forms.Form):  
    file      = forms.FileField() # for creating file input  