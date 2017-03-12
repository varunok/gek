# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from articles.models import Sections, Articles


class SectionsAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created')

admin.site.register(Sections, SectionsAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created')

admin.site.register(Articles, ArticlesAdmin)
