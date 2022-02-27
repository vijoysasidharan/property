from django.contrib.auth import get_user_model, authenticate, login as validate, logout as getout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(user)
        exit
        if user is not None:            
            validate(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'account/login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.password = make_password(request.POST.get('password'))
            form.instance.is_active = True
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse(f'error: {form.errors}')
        '''first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            user.is_active=True
            user.save()
            return HttpResponse('success')'''
    else:  
        return render(request, 'account/register.html', {'form': RegistrationForm})

def logout(request):
    getout(request)
    return redirect("login")
