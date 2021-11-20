from django.db import models

# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmplyoeeId = models.AutoField(primary_key=True)
    EmplyoeeName = models.CharField(max_length=500)
    Departmen = models.CharField(max_length=500)
    DateOfJoing = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
    