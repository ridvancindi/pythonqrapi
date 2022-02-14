
from django.db import router
from RestorantAPI import views
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    # re_path(r'^restorantApi',views.RestorantApi),
    # re_path(r'^restorantApi/',views.RestorantApi),
    re_path(r'^categoryApi$',views.CategoryApi),
    re_path(r'^categoryApi/([0-9]+)$',views.CategoryApi),
    path('asd/<str:rest_Code>',views.type_modele_new),
    re_path('home',views.home,name="home"),
    re_path('catlist',views.catList,name="catlist"),
    path('restorantApi/<str:id>',views.RestorantApi),
    path('delete/<str:cat_Code>',views.deleteCategory,name = "delete"),
    path('edit/<str:cat_Code>',views.edit),
    path('product/<str:cat_Code>/<int:id>',views.homes),
]
