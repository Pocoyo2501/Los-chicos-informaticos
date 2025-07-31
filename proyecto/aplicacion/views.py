
from django.shortcuts import render

def home(request):
    return render(request, 'index4.html')  # o el que prefieras como inicio


def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro/usuario.html', {'form': form})


from django.urls import reverse
from django.http import HttpResponse

def debug_urls(request):
    try:
        url = reverse('index3')
        return HttpResponse(f'index3 URL: {url}')
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')


from django.contrib.auth import login
from .forms import EmailLoginForm

def login_email(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('index')  # o a donde desees ir
    else:
        form = EmailLoginForm()
    return render(request, 'index4.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EmailLoginForm

def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('index')  # Asegúrate que exista esta vista o URL
    else:
        form = EmailLoginForm()

    return render(request, 'login.html', {'form': form})

