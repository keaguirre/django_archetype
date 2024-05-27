# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'base.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('/', {'messages': messages, 'user': user.email})
        
        else:
            error_msj= messages.error(request, 'Invalid email or password')
            return render(request, 'login.html', {'title': error_msj })
    else:
        return render(request, 'login.html', {'title': 'Login'})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully registered')
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
        logout_msj = messages.success(request, 'You have successfully logged out')
    elif messages.error:
        logout_msj = messages.error(request, 'Error logging out')
    else:
        logout_msj = messages.error(request, 'Error logging out')
    
    logout(request)
    return redirect('/', logout_msj)

def register_page(request):
    return render(request, 'register.html')