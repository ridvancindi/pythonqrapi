import re
from django.shortcuts import redirect, render

from User.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def mobile(request):

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False
@csrf_exempt
def index(request):
    if mobile(request):
        is_mobile = True
    else:
        is_mobile = False
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username ,password = password)
        if user is None:
            messages.error(request,"Kullanıcı Adı Veya Parola Hatalı")
            print("de")
        else:
            login(request,user)
            return redirect("home")
    if is_mobile==True:
        return render(request,"loginmb.html",context)
    else :
        return render(request,"loginweb.html",context)
    
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
    return redirect("/")