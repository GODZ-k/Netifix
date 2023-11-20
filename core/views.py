from django.shortcuts import render
from detail.models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    item=movie.objects.all()
    paginatordata=Paginator(item,1)
    page_no=request.GET.get("page")
    finaldata=paginatordata.get_page(page_no)
    lastpage=finaldata.paginator.num_pages
    total_page_no=[n+1 for n in range(lastpage)]
    hot_thrill=hot_thrills.objects.all()
    trend=trending.objects.all()
    movie_tags=Tags.objects.all()
    recomanded1=poster1.objects.all()
    recomanded2=poster2.objects.all()
    recomanded3=poster3.objects.all()
    Scifi=movie.objects.filter(category__category="Scifi")
    Action=movie.objects.filter(category__category="Action")
    Advanture=movie.objects.filter(category__category="Advanture")
    Comedy=movie.objects.filter(category__category="Comedy")
    Fantasy=movie.objects.filter(category__category="Fantasy")
    History=movie.objects.filter(category__category="History")
    Horror=movie.objects.filter(category__category="Horror")
    Thriller=movie.objects.filter(category__category="Thriller")
    Mystery=movie.objects.filter(category__category="Mystery")
    Romance=movie.objects.filter(category__category="Romance")
    data={
        # pagination
        "items": finaldata,
        "lastpage":lastpage,
        "total_page_no":total_page_no,
        # hot thrills
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
        "movie_tags":movie_tags

    }
    return render(request, "index.html",data)

def dmca(request):
    return render(request,"dmca.html")

def About(request):
    return render(request,"About.html")

def Netflix(request):
    items=movie.objects.filter(tags__name="Netflix")
    data={
        "items":items
    }
    return render(request,"Netflix.html",data)

def disneyplus(request):
    items=movie.objects.filter(tags__name="Disneyplus")
    data={
        "items":items
    }
    return render(request,"disney+.html",data)


def Amazonprime(request):
    items=movie.objects.filter(tags__name="Amazonprime")
    data={
        "items":items
    }
    return render(request,"Amazonprime.html",data)

def Browse(request):
    return render(request,"Browse.html")