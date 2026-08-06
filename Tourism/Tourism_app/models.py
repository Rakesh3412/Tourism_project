from django.db import models

# Create your models here.

class Homepage_video(models.Model):
    about_india = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to="About_video",null=True,blank=True)
    image = models.ImageField(upload_to="About_image",null=True,blank=True)
    