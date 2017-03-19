from django.contrib import admin
from solo.admin import SingletonModelAdmin

from admin2.models import Settings

admin.site.register(Settings, SingletonModelAdmin)
