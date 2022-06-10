from difflib import restore
from distutils.command import upload
from django import forms

from .models import *
class ProductForm(forms.ModelForm):
    def __init__ (self, rest_Code, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(restorant_id=rest_Code), required=False, help_text="Company")
    class Meta:
        model = Product
        fields = ('category','name','product_Img','price','pro_contents',"is_active")
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','cat_img')