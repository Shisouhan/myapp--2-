"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup', signup),
    path('addUser',addUser),
    path('login',login),
    path('loginForm',loginForm),
    path('logout',logout),
    path('art/<Art_id>', art),
    path('art/playList/<song_id>',playlist),
    path('art/playList/createplaylistwithsong/<song_id>',createplaylistwithsong),
    path('art/playList/createplaylistwithsong/addplaylistwithsong/<song_id>',addplaylistwithsong),
    path('createplaylist',createplaylist),
    path('detailplaylist/<playlist_id>',detailplaylist),
    path('addtoplaylist/<songs_id>/<playlist_id>',addtoplaylist),
    path('delete/<song_id>/<playlist_id>',deletesong),
    path('deleteplaylist/<playlist_id>',deleteplaylist),
    path('songInAlbum', songInAlbum),
    path('songDetail', songDetail),
]
