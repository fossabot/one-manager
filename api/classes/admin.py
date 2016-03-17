from django.contrib import admin
from classes.models import Classes, Semester


class ClassesAdmin(admin.ModelAdmin):
    pass


class SemestersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Classes, ClassesAdmin)
admin.site.register(Semester, SemestersAdmin)
