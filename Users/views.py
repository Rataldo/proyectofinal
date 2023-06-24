from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm, UpdatePasswordForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# Create your views here.

#Vista de Login request

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "ReneApp/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "ReneApp/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "ReneApp/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Users/login.html", {"form": form})



#Registro de Usuario

def register(request):

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"ReneApp/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        # form = UserCreationForm()       
        form = UserRegisterForm()     

    return render(request,"Users/registro.html" ,  {"form":form})


#logout por medio de views (explicado en clase  23)
class Logout(LogoutView): 
    template_name = "Users/logout.html"
    
    
    
#Update de info del usuario
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, "ReneApp/index.html")  # Redirigir a la página principal después de la actualización exitosa

    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "Users/update_profile.html", {"form": form})


#Updatre de contraseña

@login_required
def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, "ReneApp/index.html")    # Redirige a la página principal después de actualizar la contraseña
    else:
        form = UpdatePasswordForm(request.user)

    return render(request, 'Users/update_password.html', {'form': form})


