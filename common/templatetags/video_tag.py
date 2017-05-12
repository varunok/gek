# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter(name='convert_to_frame')
def convert_to_frame(video):
    if not video:
        return ''
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
    if not video:
        return ''
    iframe = '<iframe width="566" height="368" src="https://www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'
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
    if not video:
        return ''
    iframe = '<iframe width="595" height="340" src="https://www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'
    if 'iframe' not in video:
        try:
            video = video.split('/')[-1]
            iframe = iframe.format(video)
            return iframe
        except:
            return 'Неверний формат кода видео'
    return video


@register.filter(name='get_video_code')
def get_video_code(video):
    if not video:
        return ''
    if 'iframe' in video:
        tag_list = video.split(' ')
        src = [src for src in tag_list if 'src' in src]
        if src:
            code = src[0].split('/')[-1]
            if '?' in code:
                code = code.split('?')[0]
            return code
    else:
        code = video.split('/')[-1]
        if '?' in code:
            code = code.split('?')[0]
        return code
    return ''


