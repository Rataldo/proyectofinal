from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MemeFormulario, EditarMemeForm
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meme
from django.views import View

# Create your views here.

def index(request):
    
    return render(request, "ReneApp/index.html")


def about(request):
    
    return render(request, "ReneApp/about.html")

#Agregar memes

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

#listar memes subidos por el usuario
@login_required
def mis_memes(request):
    memes = Meme.objects.filter(user=request.user)
    return render(request, 'ReneApp/mis_memes.html', {'memes': memes})


#Borrar memes subidos por el usuario
@login_required
def borrar_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id, user=request.user)
    if request.method == 'POST':
        meme.delete()
        return redirect('mis-memes')
    return render(request, 'ReneApp/borrar_meme.html', {'meme': meme})

#confirmar borrado
class ConfirmarBorradoMemeView(LoginRequiredMixin, View):
    def get(self, request, meme_id):
        meme = get_object_or_404(Meme, id=meme_id, user=request.user)
        return render(request, 'ReneApp/borrar_meme.html', {'meme': meme})

    def post(self, request, meme_id):
        meme = get_object_or_404(Meme, id=meme_id, user=request.user)
        meme.delete()
        return render(request, 'ReneApp/meme_eliminado.html')





#Editar memes subidos por el usuario
@login_required
def editar_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id, user=request.user)
    if request.method == 'POST':
        form = EditarMemeForm(request.POST, instance=meme)
        if form.is_valid():
            form.save()
            return redirect('mis-memes')
    else:
        form = EditarMemeForm(instance=meme)
    return render(request, 'ReneApp/editar_meme.html', {'form': form, 'meme': meme})









#clases basadas en vistas:

#ver todos los memes:

class MemeList(LoginRequiredMixin, ListView):
    model = Meme
    template_name = "ReneApp/memes_list.html"
    context_object_name = "object_list"