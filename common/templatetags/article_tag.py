from django import template

from articles.models import Articles

register = template.Library()


@register.assignment_tag
def articles():
    try:
        return Articles.objects.order_by('?')[:4]
    except:
        return ''


@register.filter(name='font_text')
def font_text(text):
    return text.replace('PFDinTextCompPro', 'Roboto').replace('font-size:24px', 'font-size:14px')
