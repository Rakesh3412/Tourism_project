from django.shortcuts import render
from .models import Homepage_video
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    data = Homepage_video.objects.all()
    return render(request,"about.html",{"data":data})

def tour_places(request):
    places = TourPlace.objects.all()
    return render(request,"my_topic.html",{"data":places})
    