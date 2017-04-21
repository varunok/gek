from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from common.admin import VideoInline, FAQInline, PhotoInline, TableRepairInline
from services.models import ServicesRieltor, Valuation, Repair, Cleaning, Insurance, InstallationWater, UniversalService


class ServicesRieltorAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline]


class ValuationAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline]


class RepairAdmin(SingletonModelAdmin):
    inlines = [VideoInline, TableRepairInline, PhotoInline]


class InsuranceAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PhotoInline]


class CleaningAdmin(SingletonModelAdmin):
    inlines = [VideoInline, PhotoInline]


class InstallationWaterAdmin(SingletonModelAdmin):
    inlines = [VideoInline, PhotoInline, FAQInline]


class UniversalServiceAdmin(admin.ModelAdmin):
    inlines = [VideoInline, PhotoInline, FAQInline]


admin.site.register(ServicesRieltor, ServicesRieltorAdmin)
admin.site.register(Valuation, ValuationAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Insurance, RepairAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(InstallationWater, InstallationWaterAdmin)
admin.site.register(UniversalService, UniversalServiceAdmin)