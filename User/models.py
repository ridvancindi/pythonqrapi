from django.db import models
from django.contrib.auth.models import User

from RestorantAPI.models import Restorant
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    restorant = models.ForeignKey(Restorant, to_field="rest_Code", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username