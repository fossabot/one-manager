# -*- coding: utf-8 -*-
from django.contrib import admin
from score.models import Score, ScoreData


class ScoreAdmin(admin.ModelAdmin):
    pass


class ScoreDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Score, ScoreAdmin)
admin.site.register(ScoreData, ScoreDataAdmin)
