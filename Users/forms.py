from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


#Registro de usuarios
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_text = {k: "" for k in fields}


#Actualizacion de info de usuarios
from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        


from django.contrib.auth.forms import PasswordChangeForm

class UpdatePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'placeholder': 'Contraseña actual'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Nueva contraseña'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirmar nueva contraseña'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user





