from django.shortcuts import redirect, render

from User.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username ,password = password)
        if user is None:
            messages.error(request,"Kullanıcı Hadı Veya Parola Hatalı")
            return render(request,"index.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("home")
    return render(request,"index.html",context)
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, 'Başarıyla Kayıt Oldunuz.')
        return redirect("home")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
def logoutuser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("/")