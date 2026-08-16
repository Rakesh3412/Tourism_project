from django.db import models
import uuid
# Create your models here.

class Homepage_video(models.Model):
    about_india = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to="About_video",null=True,blank=True)
    image = models.ImageField(upload_to="About_image",null=True,blank=True)

class State(models.Model):
    State_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    State_name=models.CharField(max_length=70)
    State_description=models.TextField()
    State_img=models.ImageField(upload_to="State_image",null=True,blank=True)
    State_loc_img=models.ImageField(upload_to="State_loc_img",null=True,blank=True)
    State_video=models.FileField(upload_to="State_vedio",null=True,blank=True)
    