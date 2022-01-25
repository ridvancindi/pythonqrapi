from difflib import restore
from django import forms

from .models import *
class ProductForm(forms.ModelForm):
    restorant = models.ForeignKey(Restorant,on_delete=models.CASCADE)
    category =  ChainedForeignKey(
        Category,
        chained_field="restorant",
        chained_model_field="restorant",
        show_all=False,
        auto_choose=True,
        sort=True)
    class Meta:
        model = Product
        fields = ('name', 'price','restorant', 'category',)

    def __init__(self, id, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)