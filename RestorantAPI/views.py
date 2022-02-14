import random
import string
from django import forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from RestorantAPI.forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from RestorantAPI.models import *
from RestorantAPI.serializers import *
from User.models import Account
# Create your views here.
@csrf_exempt
def CategoryApi(request,restorant_id):
    if request.method=='GET':
        category = Category.objects.filter(restorant_id=restorant_id)
        category_serializer=CategorySerializer(category,many=True)
        return JsonResponse(category_serializer.data,safe=False)
    elif request.method=='DELETE':
        department=Category.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def RestorantApi(request,id):
    if request.method=='GET':
        restorant = Restorant.objects.filter(rest_Code=id)
        restorant_serializer=RestorantSerializer(restorant,many=True)
        return JsonResponse(restorant_serializer.data,safe=False)
    elif request.method=='DELETE':
        album=Restorant.objects.get(EmplyoeeId=id)
        album.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
def ProductApi(request,id,cat_id):
    if request.method=='GET':
        restorant = Product.objects.filter(category=cat_id,restorant_id=id)
        restorant_serializer=ProductSerializer(restorant,many=True)
        return JsonResponse(restorant_serializer.data,safe=False)
    elif request.method=='DELETE':
        album=ProductSerializer.objects.get(EmplyoeeId=id)
        album.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
@login_required(login_url = "/")
def productadd(request,rest_Code):
    form = ProductForm(rest_Code)  
    rest_Code = request.user.account.restorant_id
    models = Category.objects.filter(restorant_id=rest_Code)
    context = {
        'form': form,
        'models':models
    } 
    if request.method == "POST":
        category = request.POST["category"]
        name = request.POST['name']
        product_Img = request.POST.get('product_Img', False)
        price = request.POST.get('price', False)
        pro_contents = request.POST.get('pro_contents', False)
        Product.objects.create(restorant_id=rest_Code,category_id=category,name=name,product_Img=product_Img,price=price,pro_contents=pro_contents)
    else: 
        form = ProductForm(rest_Code)  

    return render(request, 'productadd.html',context)
@login_required(login_url = "/")
def home(request):
    rest_Code = request.user.account.restorant_id
    models = Category.objects.filter(restorant_id=rest_Code)
    context = {
        "models":models
    } 
    return render(request,"home.html",context)
@login_required(login_url = "/")
def catList(request):
    rest_Code = request.user.account.restorant_id
    models = Category.objects.filter(restorant_id=rest_Code)
    context = {
        "models":models
    } 
    return render(request,"list.html",context)
@login_required(login_url = "/")
def deleteCategory(request,cat_Code):
    deleteCategory = get_object_or_404(Category,cat_Code = cat_Code)
    deleteCategory.delete()
    messages.success(request,"Başarıyla Silindi.")
    return redirect("catlist")
@csrf_exempt
@login_required(login_url = "/")
def edit(request,cat_Code):
    editmoney = get_object_or_404(Category,cat_Code=cat_Code)
    form = CategoryForm(request.POST or None,request.FILES or None,instance=editmoney)
    if form.is_valid():
        editmoney =form.save(commit=False)
        editmoney.save()
        messages.success(request,"Başarıyla Düzenlendi")
        return redirect("catlist")
    return render(request,"edit.html",{"form":form})
@login_required(login_url = "/")
def homes(request,cat_Code,id):
    rest_Code = request.user.account.restorant_id
    models = Product.objects.filter(category_id=id)
    context = {
        "models":models
    } 
    return render(request,"productList.html",context)