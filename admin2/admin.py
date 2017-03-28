from django.contrib import admin
from solo.admin import SingletonModelAdmin

from admin2.models import Settings, StaticPageModel

admin.site.register(Settings, SingletonModelAdmin)
admin.site.register(StaticPageModel)

