from django.contrib import admin
from login.models import OneManagerUser


class OneManagerUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(OneManagerUser, OneManagerUserAdmin)
