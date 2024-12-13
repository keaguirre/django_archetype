# views.py
import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_login.sendgrid_mails import send_email

load_dotenv()
def home(request):
    return render(request, 'base.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
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
            print('form is valid')
            email = form.cleaned_data.get('email')  # Campo de entrada original de 'email'
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                error_msj = messages.error(request, 'Las contraseñas no coinciden')
                return render(request, 'register.html', {'title': error_msj})
            else:
                user = User.objects.create_user(email=email, password=password)
                user_auth = authenticate(request, email=email, password=password)
                from_mail = os.getenv('FROM_MAIL')
                to_email = email
                mail_subject = 'Registro exitoso'
                mail_content = f'Hola, {email}, te has registrado con éxito en nuestra plataforma.'
                send_email(from_mail, to_email, mail_subject, mail_content)
            if user is not None:
                login(request, user_auth)
                messages.success(request, 'Registrado con éxito')

                return redirect('/', messages)
            else:
                error_msj = messages.error(request, user)
                return render(request, 'register.html', {'title': error_msj})
        else:
            print(form.is_valid(),'form is not valid')
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