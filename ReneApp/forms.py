from django import forms
from .models import Meme


#formulario para subir memes

# class MemeFormulario(forms.Form):
#     name = forms.CharField(max_length=50)
#     image = forms.ImageField()
#     caption = forms.CharField(max_length=100)

class MemeFormulario(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['name', 'image', 'caption']