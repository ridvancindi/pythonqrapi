from django.contrib import admin

from RestorantAPI.models import *

# Register your models here.
admin.site.register(Restorant)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "restorant")
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "restorant","category")