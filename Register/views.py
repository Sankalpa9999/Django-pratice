
from django.shortcuts import render, redirect


from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import UserRegisterForm
from django.contrib import messages
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            form.save()
            print ("HEllo world")
            messages.success(request, f'Account created for {username}')
            return redirect('index')

        else:
            print (form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'Register/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print (user)
        if user is not None:
            login(request, user)
            print ("Succes")
            return redirect('index')

        else:
            messages.info(request, 'Username or password is incorrect')
            print ("Wrong Password")
            
    return render(request, 'Register/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')