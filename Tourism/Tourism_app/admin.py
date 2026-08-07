from django.contrib import admin
from .models import Homepage_video
from .models import State

# Register your models here.
class Homepage_admin(admin.ModelAdmin):
    list_display = ["about_india","video","image"]
admin.site.register(Homepage_video,Homepage_admin)


class Statepage_admin(admin.ModelAdmin):
    list_display_1 = ["state_id","state_name","description","state_image","location"]
admin.site.register(State,Statepage_admin)