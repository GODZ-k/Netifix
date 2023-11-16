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
    Scifi=movie.objects.filter(category__category="scifi")
    Action=movie.objects.filter(category__category="action")
    Advanture=movie.objects.filter(category__category="advanture")
    Comedy=movie.objects.filter(category__category="comedy")
    Fantasy=movie.objects.filter(category__category="fantasy")
    History=movie.objects.filter(category__category="history")
    Horror=movie.objects.filter(category__category="horror")
    Thriller=movie.objects.filter(category__category="thriller")
    Mystery=movie.objects.filter(category__category="mystery")
    Romance=movie.objects.filter(category__category="romance")
    data={
        "items": item,
        "slideshow": hot_thrill,
        "trend":trend,
        "recomanded1":recomanded1,
        "recomanded2":recomanded2,
        "recomanded3":recomanded3,
        "Scifi":Scifi,
        "Action":Action,
        "Advanture":Advanture,
        "Comedy":Comedy,
        "Fantasy":Fantasy,
        "History":History,
        "Horror":Horror,
        "Thriller":Thriller,
        "Mystery":Mystery,
        "Romance":Romance,

    }
    return render(request, "index.html",data)
