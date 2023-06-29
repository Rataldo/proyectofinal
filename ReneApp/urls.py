from django.urls import path 
from ReneApp import views




urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('add_memes/', views.add_meme, name="AgregarMeme"),
    path('mis_memes/', views.mis_memes, name='mis-memes'),
    path('editar_meme/<int:meme_id>/', views.editar_meme, name='editar-meme'),
    path('borrar_meme/<int:meme_id>/', views.borrar_meme, name='borrar-meme'),

]


#clases basadas en vistas api django // CRUD
urlpatterns += [
    path('memes_list/', views.MemeList.as_view(), name="memes-list"),
    path('confirmar-borrado-meme/<int:meme_id>/', views.ConfirmarBorradoMemeView.as_view(),
    name='confirmar-borrado-meme')
]