from difflib import restore
from django import forms

from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('restorant','category')

    def __init__(self, id, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)