from django import forms
from .models import Meme


#Formulario para generar meme:
class MemeFormulario(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['name', 'image', 'caption']
        
        
#Formulario para edicion de un meme:
class EditarMemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['name', 'caption']
