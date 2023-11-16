from django.shortcuts import render
from detail.models import *

# Create your views here.
def home(request):
    item=movie.objects.all()
    hot_thrill=hot_thrills.objects.all()
    trend=trending.objects.all()
    recomanded1=poster1.objects.all()
    recomanded2=poster2.objects.all()
    recomanded3=poster3.objects.all()
    category=Categories.objects.all()
    # scifi=movie.objects.filter(Categories=scifi)
    data={
        "items": item,
        "slideshow": hot_thrill,
        "trend":trend,
        "recomanded1":recomanded1,
        "recomanded2":recomanded2,
        "recomanded3":recomanded3,
        # "scifi":scifi,
        "category":category

    }
    return render(request, "index.html",data)
