from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import BookNow


def showtravelling(request):
    return render(request, 'index.html', )


def showRegister(request):
    if request.method == 'POST':
        un = request.POST['un']
        em = request.POST['em']
        psw = request.POST['psw']
        user = User.objects.create_user(username=un, email=em, password=psw)
        user.save()

    return render(request, 'Register.html')


def showlogin(request):
    if request.method == 'POST':
        unl = request.POST['unl']
        pswa = request.POST['pswa']
        user = auth.authenticate(username=unl, password=pswa)
        if user is not None:
            auth.login(request, user)
            print('login sucess')
            return redirect('../')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('../travelling')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def bookNow(request):
    if request.method == "POST":
        Fn = request.POST.get('Fn', '')
        Ln = request.POST.get('Ln', '')
        un = request.POST.get('un', '')
        cty = request.POST.get('cty', '')
        zp = request.POST.get('zp', '')
        app = BookNow(Fn=Fn, Ln=Ln, un=un, cty=cty, zp=zp)
        app.save()

    return render(request, 'BookNow.html')
