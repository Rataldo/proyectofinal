from django import forms
from .models import Meme


class MemeFormulario(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['name', 'image', 'caption']