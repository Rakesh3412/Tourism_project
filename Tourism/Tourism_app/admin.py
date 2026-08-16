from django.contrib import admin
from .models import Homepage_video
from .models import State
from .models import TourPlaces
# Register your models here.
class Homepage_admin(admin.ModelAdmin):
    list_display = ["about_india","video","image"]
admin.site.register(Homepage_video,Homepage_admin)

class State_admin(admin.ModelAdmin):
    list_display =["State_id","State_name","State_description","State_img","State_loc_img","State_video"]
admin.site.register(State,State_admin)

class TourPlaces_admin(admin.ModelAdmin):
    list_display=["Place_id","State_name","Place_name","Place_description","Place_img","Place_loc_img"]
admin.site.register(TourPlaces,TourPlaces_admin)
