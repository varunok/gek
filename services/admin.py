from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from common.admin import VideoInline, FAQInline
from services.models import ServicesRieltor

class ServicesRieltorAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline]

admin.site.register(ServicesRieltor, ServicesRieltorAdmin)
