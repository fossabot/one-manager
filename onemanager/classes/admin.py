from django.contrib import admin
from onemanager.classes.models import School, Classes, Semester


class SchoolAdmin(admin.ModelAdmin):
    pass


class ClassesAdmin(admin.ModelAdmin):
    pass


class SemestersAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Semester, SemestersAdmin)
