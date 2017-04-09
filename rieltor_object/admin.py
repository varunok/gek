# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from common.admin import PhotoInline, VideoInline
from rieltor_object.models import Building

class BuildingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]

admin.site.register(Building, BuildingAdmin)
