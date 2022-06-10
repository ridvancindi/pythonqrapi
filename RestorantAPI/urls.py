
from django.db import router
from django.conf import settings  
from django.conf.urls.static import static  
from RestorantAPI import views
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    # re_path(r'^restorantApi',views.RestorantApi),
    # re_path(r'^restorantApi/',views.RestorantApi),
    re_path(r'^categoryApi$',views.CategoryApi),
    re_path(r'^categoryApi/([0-9]+)$',views.CategoryApi),
    path('productadd/<str:rest_Code>',views.productadd),
    path('deleteproduct/<int:id>',views.productDelete,name = "productDelete"),
    path('categoryadd/<str:rest_Code>',views.categoryAdd),
    re_path('home',views.home,name="home"),
    re_path('catlist',views.catList,name="catlist"),
    path('restorantApi/<str:id>',views.RestorantApi),
    path('delete/<str:cat_Code>',views.deleteCategory,name = "delete"),
    path('edit/<str:cat_Code>',views.edit),
    path('product/<str:cat_Code>/<int:id>',views.homes),
    path('deneme',views.productlistpage),
]
