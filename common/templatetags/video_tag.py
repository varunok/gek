# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter(name='convert_to_frame')
def convert_to_frame(video):
    iframe = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'
    if 'iframe' not in video:
        try:
            video = video.split('/')[-1]
            iframe = iframe.format(video)
            return iframe
        except:
            return 'Неверний формат кода видео'
    return video


@register.filter(name='convert_to_frame_slider')
def convert_to_frame_slider(video):
    iframe = '<iframe width="566" height="368" src="https://www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'
    if 'iframe' not in video:
        try:
            video = video.split('/')[-1]
            iframe = iframe.format(video)
            return iframe
        except:
            return 'Неверний формат кода видео'
    return video