from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework import status
from EmployeeApp.forms import *
from EmployeeApp.models import *
from EmployeeApp.serializers import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response  # Import this for Response
from rest_framework.viewsets import GenericViewSet

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
def RestorantApi(request,res_code):
    if request.method=='GET':
        category = Category.objects.filter(restorant_id=res_code)
        category_serializer=CategorySerializer(category,many=True)
        restorant = Restorant.objects.filter(rest_Code=res_code)
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
def new_product(request,id):
    if request.method == 'POST':
        form = ProductForm(id)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products_list')
    else:
        form = ProductForm(id)
    return render(request, 'expenses.html', {'form': form})
class MeMixin:
    @action(methods=['get'], detail=False)
    def me(self, request):
        serializer = self.get_serializer_class()
        data = serializer(
            **self.get_me_config()
        ).data
        return Response(data, status=status.HTTP_200_OK)

