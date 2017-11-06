# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

class MetricInline(admin.TabularInline):
	model = models.Metric

class CategoryAdmin(admin.ModelAdmin):
	inlines = [
		MetricInline
	]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Game)
admin.site.register(models.Score)

