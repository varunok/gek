# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from easy_thumbnails.files import get_thumbnailer

from django import template
from banners.models import SideBanner, DownBanner

register = template.Library()


class BannerNode(template.Node):
    def __init__(self, code=None, image=None):
        self.code = code
        self.image = image

    def render(self, context):
        if self.code:
            return self.code
        elif self.image:
            return self.image
        else:
            return ''


@register.tag('sidebanner')
def sidebanner(parser, token):
    sideban = SideBanner.get_solo()
    if sideban.active_code:
        return BannerNode(sideban.code)
    else:
        if sideban.image:
            image = '<div class="block banner"><a href="{1}"><div class="field_image"><img src="{0}" alt=""></div></a></div>'.format(
                sideban.image.url,
                sideban.link
            )
            return BannerNode(image)
    return BannerNode('')


@register.tag('downbanner')
def downbanner(parser, token):
    downban = DownBanner.get_solo()
    if downban.active_code:
        return BannerNode(downban.code)
    else:
        if downban.image:
            thumbnailer = get_thumbnailer(downban.image)
            thumbnail_options = {'crop': 'smart'}
            thumbnail_options.update({'size': (970, 250)})
            image_thumb = thumbnailer.get_thumbnail(thumbnail_options)
            image_thumb.name = '/media/' + image_thumb.name
            image = '<div class="block region_banner"><a href="{1}"><div class="field_banner"><img src="{0}" alt=""></div></a></div>'.format(
                image_thumb,
                downban.link
            )
            return BannerNode(image)
    return BannerNode('')
