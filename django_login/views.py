# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'base.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión de forma exitosa')
            return redirect('/', {'messages': messages, 'user': user.email})
        
        else:
            error_msj= messages.error(request, 'Email o contraseña incorrectos')
            return render(request, 'login.html', {'title': error_msj })
    else:
        return render(request, 'login.html', {'title': 'Login'})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Campo de entrada original de 'email'
            password = form.cleaned_data.get('password1')
            username = email.split('@')[0]  # Parte antes de '@' para el username y guarda email desde el 'username' como correo que proveniente del formulario en el campo de email
            user = User.objects.create_user(username=username, email=email, password=password)
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registrado con éxito')
                return redirect('/', messages)
            else:
                error_msj = messages.error(request, user)
                return render(request, 'register.html', {'title': error_msj})
        else:
            error_msj = messages.error(request, str(form.errors))
            return render(request, 'register.html', {'title': error_msj})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def logout_user(request):
    if messages.success:
        logout_msj = messages.success(request, 'Has cerrado sesión de forma exitosa')
    elif messages.error:
        logout_msj = messages.error(request, 'Error al cerrar sesión')
    else:
        logout_msj = messages.error(request, 'Error al cerrar sesión')
    
    logout(request)
    return redirect('/', logout_msj)

def register_page(request):
    return render(request, 'register.html')