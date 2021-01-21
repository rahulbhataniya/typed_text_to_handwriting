from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user_name=models.CharField(max_length=100)
    imagefile1=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile2=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile3=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile4=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile5=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile6=models.FileField(upload_to="images/",null=True,verbose_name="")
    
    def __str__(self):
        return str(self.user_name)




