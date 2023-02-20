
from django.contrib import admin
from django.urls import path, include
from movie_downloader  import views 
urlpatterns = [
    path("",views.index, name='movie_downloader'),
    path("about",views.about, name='about')
]
 