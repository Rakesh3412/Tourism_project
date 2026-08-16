from django.shortcuts import render
from .models import Homepage_video
from .models import State

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    data = Homepage_video.objects.all()
    return render(request,"about.html",{"data":data})

def states(request):
    data_1 = State.objects.all()
    return render(request,"my_topic.html",{"data_1":data_1})