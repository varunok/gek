from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline

from common.models import Application, Video, FAQ, Photo, BasePacket, TextPacket, \
    MidlePacket, ExpertPacket, TableRepair, Advantage, Feed, WhatYouKnown, Process,  \
    Finish, Preparation


class PreparationInline(GenericTabularInline):
    model = Preparation
    extra = 0


class FinishInline(GenericTabularInline):
    model = Finish
    extra = 0


class ProcessInline(GenericTabularInline):
    model = Process
    extra = 0


class VideoInline(GenericTabularInline):
    model = Video
    extra = 0


class WhatYouKnownInline(GenericTabularInline):
    model = WhatYouKnown
    extra = 0


class FAQInline(GenericTabularInline):
    model = FAQ
    extra = 0


class PhotoInline(GenericTabularInline):
    model = Photo
    extra = 0


class TextPacketInline(GenericTabularInline):
    model = TextPacket
    extra = 0


class TableRepairInline(GenericTabularInline):
    model = TableRepair
    extra = 0


class AdvantageInline(GenericTabularInline):
    model = Advantage
    extra = 0


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created')


class BasePacketAdmin(admin.ModelAdmin):
    inlines = [TextPacketInline]


class MidlePacketAdmin(admin.ModelAdmin):
    inlines = [TextPacketInline]


class ExpertPacketAdmin(admin.ModelAdmin):
    inlines = [TextPacketInline]


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Video)
admin.site.register(FAQ)
admin.site.register(TableRepair)
admin.site.register(Photo)
admin.site.register(Feed)
admin.site.register(BasePacket, BasePacketAdmin)
admin.site.register(MidlePacket, MidlePacketAdmin)
admin.site.register(ExpertPacket, ExpertPacketAdmin)
admin.site.register(Advantage)
admin.site.register(TextPacket)
admin.site.register(Process)
admin.site.register(Preparation)
admin.site.register(Finish)

