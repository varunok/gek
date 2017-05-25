from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from solo.admin import SingletonModelAdmin

# Register your models here.
from common.admin import VideoInline, FAQInline, PhotoInline, TableRepairInline
from services.models import ServicesRieltor, Valuation, Repair, Cleaning, Insurance, InstallationWater, \
    UniversalService, Partner


class PartnerInline(GenericTabularInline):
    model = Partner
    extra = 0


class ServicesRieltorAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PartnerInline]


class ValuationAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PartnerInline]


class RepairAdmin(SingletonModelAdmin):
    inlines = [VideoInline, TableRepairInline, PhotoInline, PartnerInline]


class InsuranceAdmin(SingletonModelAdmin):
    inlines = [VideoInline, FAQInline, PhotoInline, PartnerInline]


class CleaningAdmin(SingletonModelAdmin):
    inlines = [VideoInline, PhotoInline, PartnerInline]


class InstallationWaterAdmin(SingletonModelAdmin):
    inlines = [VideoInline, PhotoInline, FAQInline, PartnerInline]


class UniversalServiceAdmin(admin.ModelAdmin):
    inlines = [VideoInline, PhotoInline, FAQInline, PartnerInline]


admin.site.register(ServicesRieltor, ServicesRieltorAdmin)
admin.site.register(Valuation, ValuationAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Insurance, RepairAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(InstallationWater, InstallationWaterAdmin)
admin.site.register(UniversalService, UniversalServiceAdmin)
admin.site.register(Partner)
