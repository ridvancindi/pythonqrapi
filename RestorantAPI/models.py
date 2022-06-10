import os
from pyexpat import model
import random
import string
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey 
def deneme():
    allowed_chars = ''.join((string.ascii_letters))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))
    return unique_id
def rest_file_name(instance, filename):
    return '/'.join(filter(None, ("Image",instance.rest_Code, filename)))
def cat_file_name(instance, filename):
    return '/'.join(filter(None, ("Image",instance.restorant_id,instance.name,"Cat Logo "+filename)))
def pro_file_name(instance, filename):
    deneme = list(Category.objects.filter(id = instance.category_id).only('name')[:1])[0]
    return '/'.join(filter(None, ("Image",instance.restorant_id ,str(deneme),"Product Logo "+filename)))
class Restorant(models.Model):
    rest_name = models.CharField(max_length=100)
    rest_createDate = models.DateField()
    rest_Phone = models.CharField(max_length=12)
    rest_Code =  models.CharField(max_length = 12,blank=True,editable=False,default=deneme,unique=True)
    rest_img = models.ImageField(upload_to =rest_file_name)
    def delete(self, using=None, keep_parents=False):
        self.rest_img.storage.delete(self.rest_img.name)
        super().delete()
    def __str__(self):
        return self.rest_name
class Category(models.Model):
    restorant = models.ForeignKey(Restorant, to_field="rest_Code", related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cat_img = models.ImageField(upload_to =cat_file_name)
    cat_Code =  models.CharField(max_length = 12,blank=True,editable=False,default=deneme,unique=True)
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.cat_img.storage, self.cat_img.path
        # Delete the model before the file
        super(Category, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
class Product(models.Model):
    restorant = models.ForeignKey(Restorant, to_field="rest_Code",on_delete=models.CASCADE)
    category = ChainedForeignKey(
        Category,
        chained_field="restorant",
        chained_model_field="restorant",
        show_all=False,
        auto_choose=True,
        sort=True,
        related_name='product',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_Img = models.ImageField(upload_to =pro_file_name)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_active = models.BooleanField(null=True,default=True)
    pro_contents = models.TextField()
    discount_price = models.DecimalField(decimal_places=2, max_digits=10,default=None, blank=True, null=True)
    def delete(self, using=None, keep_parents=False):
        print(self.song.name)
        self.song.storage.delete(self.song.name)
        self.product_Img.storage.delete(self.song.name)
        super().delete()
    def __str__(self):
        return self.name
