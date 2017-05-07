from django import template
import re

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    try:
        return field.as_widget(attrs={"class": css})
    except AttributeError:
        return ''


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


@register.filter(name='add_style')
def add_style(field, style):
    try:
        return field.as_widget(attrs={"style": style})
    except AttributeError:
        return ''

@register.filter(name='add_attr')
def add_attr(field, style):
    index_tag = field.find('>')
    templ_tag = field[0:index_tag] + ' ' + style + field[index_tag:]
    return templ_tag
