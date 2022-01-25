from itertools import product
from rest_framework import serializers
from EmployeeApp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'product_Img']

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name','rest_Code','product']

class RestorantSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Restorant
        fields = (['rest_name' , 'rest_createDate' , 'rest_Phone' , 'rest_Code' , 'category'])
    