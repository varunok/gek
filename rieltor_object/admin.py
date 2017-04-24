# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline

from common.admin import PhotoInline, VideoInline
from rieltor_object.models import Building, Ofice, NewBuilding, Daily, Infrastructure, Accommodations, District, \
    DailyDistrict, ApartmentHas
from common.models import ApartmentNext


class BuildingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


class OficeAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


class NewBuildingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


class DailyAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]

admin.site.register(Building, BuildingAdmin)
admin.site.register(Ofice, OficeAdmin)
admin.site.register(NewBuilding, NewBuildingAdmin)
admin.site.register(Daily, DailyAdmin)
admin.site.register(District)
admin.site.register(DailyDistrict)
admin.site.register(Infrastructure)
admin.site.register(ApartmentHas)
admin.site.register(Accommodations)
admin.site.register(ApartmentNext)
