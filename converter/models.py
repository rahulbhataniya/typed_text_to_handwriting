from django.db import models


class Image(models.Model):
    imagefile=models.FileField(upload_to="images/",null=True,verbose_name="")
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name+":"+str(self.imagefile)


