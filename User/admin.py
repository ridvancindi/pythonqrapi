from django.contrib import admin

from User.models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'
class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline,)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)