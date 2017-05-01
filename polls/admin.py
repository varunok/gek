# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from polls.models import Polls, Choice, Question, Result

admin.site.register(Polls)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Result)