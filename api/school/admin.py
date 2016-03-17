from django.contrib import admin
from school.models import School


class SchoolAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
