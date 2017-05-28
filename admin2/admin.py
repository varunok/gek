from django.contrib import admin
from solo.admin import SingletonModelAdmin

from admin2.models import Settings, IndexPageModel, NewBuildingPageModel, DailyPageModel, BuildingPageModel, \
    OfisPageModel, TrustPageModel, ContactPageModel, ActiveFranchise, SettingsFranchise, SettingsAddress, \
    Help

admin.site.register(Settings, SingletonModelAdmin)
admin.site.register(IndexPageModel, SingletonModelAdmin)
admin.site.register(NewBuildingPageModel, SingletonModelAdmin)
admin.site.register(DailyPageModel, SingletonModelAdmin)
admin.site.register(BuildingPageModel, SingletonModelAdmin)
admin.site.register(OfisPageModel, SingletonModelAdmin)
admin.site.register(TrustPageModel, SingletonModelAdmin)
admin.site.register(ContactPageModel, SingletonModelAdmin)
admin.site.register(ActiveFranchise, SingletonModelAdmin)
admin.site.register(SettingsFranchise, SingletonModelAdmin)
admin.site.register(SettingsAddress, SingletonModelAdmin)
admin.site.register(Help)
