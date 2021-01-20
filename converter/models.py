from django.db import models


class Image(models.Model):
    imagefile1=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile2=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile3=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile4=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile5=models.FileField(upload_to="images/",null=True,verbose_name="")
    imagefile6=models.FileField(upload_to="images/",null=True,verbose_name="")
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name


