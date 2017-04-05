from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline

from common.models import Application, Video, FAQ, Photo


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created')

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Video)
admin.site.register(FAQ)
admin.site.register(Photo)


class VideoInline(GenericTabularInline):
    model = Video
    extra = 0

class FAQInline(GenericTabularInline):
    model = FAQ
    extra = 0

class PhotoInline(GenericTabularInline):
    model = Photo
    extra = 0
