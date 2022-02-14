from itertools import product
from rest_framework import serializers
from RestorantAPI.models import *
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
class AttrPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name','cat_img','product']

class RestorantSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Restorant
        fields = (['rest_name' , 'rest_createDate' , 'rest_Phone' , 'rest_Code','rest_img' , 'category'])