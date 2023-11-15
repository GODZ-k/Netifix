from django.shortcuts import render
from detail.models import *

# Create your views here.
def home(request):
    item=movie.objects.all()
    hot_thrill=hot_thrills.objects.all()
    trend=trending.objects.all()
    data={
        "items": item,
        "slideshow": hot_thrill,
        "trend":trend
    }
    return render(request, "index.html",data)
