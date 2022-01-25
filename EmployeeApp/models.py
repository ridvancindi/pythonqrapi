from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

from smart_selects.db_fields import ChainedForeignKey
class Restorant(models.Model):
    rest_name = models.CharField(max_length=100)
    rest_createDate = models.DateField()
    rest_Phone = models.CharField(max_length=12)
    rest_Code = models.CharField(max_length=8,unique=True)
    def __str__(self):
        return self.rest_name
class Category(models.Model):
    restorant = models.ForeignKey(Restorant, to_field="rest_Code", related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rest_Code = models.CharField(max_length=8)
    def __str__(self):
        return self.name
class Product(models.Model):
    restorant = models.ForeignKey(Restorant, to_field="rest_Code",on_delete=models.CASCADE)
    category = ChainedForeignKey(
        Category,
        chained_field="restorant",
        chained_model_field="restorant",
        show_all=False,
        auto_choose=True,
        sort=True,
        related_name='product')
    name = models.CharField(max_length=50)
    product_Img = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return self.name
