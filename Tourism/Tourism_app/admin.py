from django.contrib import admin
from .models import Homepage_video

# Register your models here.
class Homepage_admin(admin.ModelAdmin):
    list_display = ["about_india","video","image"]
admin.site.register(Homepage_video,Homepage_admin)
