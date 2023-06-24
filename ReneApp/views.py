from django.shortcuts import render
from .models import *
from .forms import MemeFormulario
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    
    return render(request, "ReneApp/index.html")


def about(request):
    
    return render(request, "ReneApp/about.html")

#formulario para agregar memes
# @login_required
# def add_meme(request):
#     if request.method == "POST":
#         meme_formulario = MemeFormulario(request.POST, request.FILES)
#         if meme_formulario.is_valid():
#             meme = meme_formulario.save()
#             return render(request, "ReneApp/index.html")
#     else:
#         meme_formulario = MemeFormulario()
    
#     return render(request, "ReneApp/add_memes.html", {"meme_formulario": meme_formulario})

@login_required
def add_meme(request):
    if request.method == "POST":
        meme_formulario = MemeFormulario(request.POST, request.FILES)
        if meme_formulario.is_valid():
            meme = meme_formulario.save(commit=False)
            meme.user = request.user
            meme.save()
            return render(request, "ReneApp/index.html")
    else:
        meme_formulario = MemeFormulario()
    
    return render(request, "ReneApp/add_memes.html", {"meme_formulario": meme_formulario})







#clases basadas en vistas:

#ver todos los memes:

class MemeList(LoginRequiredMixin, ListView):
    model = Meme
    template_name = "ReneApp/memes_list.html"
    context_object_name = "object_list"