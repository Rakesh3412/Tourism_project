from django.shortcuts import render
from .models import Homepage_video

# Create your views here.
def home(request):
    return render(request,"Home.html")

def about(request):
    data = Homepage_video.objects.all()
    return render(request,"about.html",{"data":data})
