# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline

from common.admin import PhotoInline, VideoInline
from rieltor_object.models import Building, Ofice, NewBuilding, Infrastructure, Accommodations, District


class BuildingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


class OficeAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


class NewBuildingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]

admin.site.register(Building, BuildingAdmin)
admin.site.register(Ofice, OficeAdmin)
admin.site.register(NewBuilding, NewBuildingAdmin)
admin.site.register(District)
admin.site.register(Infrastructure)
admin.site.register(Accommodations)
