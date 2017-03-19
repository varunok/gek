from django import template
import re

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})\

@register.filter(name='addid')
def addid(field, id):
    return field.as_widget(attrs={"id": id})

@register.filter(name='addrows')
def addrows(field, rows):
    if 'rows' in field:
        regex = r"rows=\"\d*\""
        repl = ''.join(['rows="', rows, '"'])
        field = re.sub(regex, repl, field, flags=re.IGNORECASE)
    return field
