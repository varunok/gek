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
    else:
        try:
            video_item = video.split(' ')
            for ele in video_item:
                if 'watch' in ele:
                    el = ele.split('=')[-1]
                    iframe = iframe.format(el)
            return iframe
        except:
            return 'Неверний формат кода видео'
    # return video


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
    else:
        try:
            video_item = video.split(' ')
            for ele in video_item:
                if 'watch' in ele:
                    el = ele.split('=')[-1]
                    iframe = iframe.format(el)
            return iframe
        except:
            return 'Неверний формат кода видео'


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


@register.filter(name='convert_panorama')
def convert_panorama(panorama):
    if not panorama:
        return panorama
    code = '<iframe src="https://www.google.com/maps/embed?{code} ' \
           'width="{width}" height="{height}" ' \
           'frameborder="0" style="border:0" allowfullscreen></iframe>'
    yandex_code = '<script src="https://panoramas.api-maps.yandex.ru/embed/1.x/?lang=ru&ll=24.02731861%2C49.84294679&ost=dir%3A152.89056442361806%2C9.061250000000003~span%3A119.21110794003725%2C80&size=690%2C495&l=stv"></script>'
    size = 'size={width}%2C{height}'
    if 'iframe' in panorama:
        panorama_code = panorama.split(' ')[1].split('?')[-1]
        return code.format(code=panorama_code, width='542', height='293')
    if 'yandex' in panorama:
        panorama_list = panorama.split('&')
        for index, ele in enumerate(panorama_list):
            if 'size=' in ele:
                ele = size.format(width='542', height='293')
                panorama_list[index] = ele
        return '&'.join(panorama_list)
    return panorama