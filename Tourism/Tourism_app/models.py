from django.db import models
import uuid
# Create your models here.

class Homepage_video(models.Model):
    about_india = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to="About_video",null=True,blank=True)
    image = models.ImageField(upload_to="About_image",null=True,blank=True)




class State(models.Model):
    state_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    state_name = models.CharField()
    description = models.TextField(null=True,blank=True)
    State_image = models.ImageField(upload_to="About_state_image",null=True,blank=True)
    location = models.URLField(null=True,blank=True)