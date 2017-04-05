from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from common.admin import VideoInline, FAQInline, PhotoInline
from services.models import ServicesRieltor, Valuation, Repair


class ServicesRieltorAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PhotoInline]

class ValuationAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PhotoInline]

class RepairAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PhotoInline]

admin.site.register(ServicesRieltor, ServicesRieltorAdmin)
admin.site.register(Valuation, ValuationAdmin)
admin.site.register(Repair, RepairAdmin)
