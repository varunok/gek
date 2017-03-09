from django.contrib import admin

# Register your models here.
from common.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created')

admin.site.register(Application, ApplicationAdmin)
