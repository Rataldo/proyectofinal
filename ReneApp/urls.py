from django.urls import path 
from ReneApp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('add_memes/', views.add_meme, name="AgregarMeme"),
]



#clases basadas en vistas api django // CRUD
urlpatterns += [
    path('memes_list/', views.MemeList.as_view(), name="memes-list"),
]