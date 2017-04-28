# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from common.admin import WhatYouKnownInline
from videos.models import Videos
# Register your models here.


class VideosAdmin(admin.ModelAdmin):
    inlines = [WhatYouKnownInline]


admin.site.register(Videos, VideosAdmin)
