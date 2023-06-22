from django.shortcuts import render
from .models import *
from .forms import MemeFormulario
from django.views.generic import ListView


# Create your views here.

def index(request):
    
    return render(request, "ReneApp/index.html")


def about(request):
    
    return render(request, "ReneApp/about.html")

#Formulario para agregar Meme:

# def add_meme(request):
#     if request.method == "POST":
#         meme_formulario = MemeFormulario(request.POST) # Aqui me llega la informacion del html

#         if meme_formulario.is_valid():
#             informacion = meme_formulario.cleaned_data
#             meme = Meme(name=informacion["nombre"], image=informacion["imagen"], caption=informacion["descripcion"])
#             meme.save()
#             return render(request, "ReneApp/index.html")
#     else:
#         meme_formulario = MemeFormulario()

#     return render(request, "ReneApp/add_memes.html", {"meme_formulario": meme_formulario})

def add_meme(request):
    if request.method == "POST":
        meme_formulario = MemeFormulario(request.POST, request.FILES)
        if meme_formulario.is_valid():
            meme = meme_formulario.save()
            #return redirect('index')
            return render(request, "ReneApp/index.html")
    else:
        meme_formulario = MemeFormulario()
    
    return render(request, "ReneApp/add_memes.html", {"meme_formulario": meme_formulario})









#clases basadas en vistas:

#ver todos los memes:

class MemeList(ListView):
    model = Meme
    template_name = "ReneApp/memes_list.html"
    context_object_name = "object_list"