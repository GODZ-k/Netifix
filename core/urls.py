from django.urls import path,include
from .views import *

urlpatterns = [
    path("" , home , name="home"),
    path("Dmca/",dmca, name="dmca"),
    path("About/", About ,name="about"),
    path("Netflix",Netflix,name="netflix"),
    path("Disney+",disneyplus,name="disneyplus"),
    path("Amazonprime/",Amazonprime,name="amazonprime"),
]

