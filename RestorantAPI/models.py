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
class Restorant(models.Model):
    rest_name = models.CharField(max_length=100)
    rest_createDate = models.DateField()
    rest_Phone = models.CharField(max_length=12)
    rest_Code =  models.CharField(max_length = 12,blank=True,editable=False,default=deneme,unique=True)
    rest_img = models.URLField()
    def __str__(self):
        return self.rest_name
class Category(models.Model):
    restorant = models.ForeignKey(Restorant, to_field="rest_Code", related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cat_img = models.URLField()
    cat_Code =  models.CharField(max_length = 12,blank=True,editable=False,default=deneme,unique=True)
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
        related_name='product',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_Img = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    pro_contents = models.TextField()
    def __str__(self):
        return self.name
