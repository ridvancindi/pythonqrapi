
from django.db import router
from EmployeeApp import views
from django.urls import re_path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    re_path(r'^restorantApi$',views.RestorantApi),
    re_path(r'^restorantApi/([0-9]+)$',views.RestorantApi),
    re_path(r'^categoryApi$',views.CategoryApi),
    re_path(r'^categoryApi/([0-9]+)$',views.CategoryApi),
    re_path(r'asd/([0-9]+)$',views.type_modele_new),

]
