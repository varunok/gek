# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from admin2.models import Counters, Settings
from landing.models import LandingFutor


def counter(request):
    counters = Counters.get_solo()
    carrency = Settings.get_solo().get_currency_display()
    return {
        'counter_1': counters.counter_1,
        'counter_2': counters.counter_2,
        'counter_3': counters.counter_3,
        'counter_4': counters.counter_4,
        'nac_carrency': carrency,
        'landings': LandingFutor.objects.all()

    }