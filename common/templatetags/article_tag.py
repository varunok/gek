from django import template

from articles.models import Articles

register = template.Library()


@register.assignment_tag
def articles():
    try:
        return Articles.objects.order_by('?')[:4]
    except:
        return ''