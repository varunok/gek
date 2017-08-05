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


class OrderNode(template.Node):
    TAGS = {
        'a': '<a href="{path}"><i class="fa {fa_class}"></i></a>',
        'cls_asc': 'fa-sort-asc',
        'cls_desc': 'fa-sort-desc',
        'cls_sort': 'fa-sort'
    }

    def __init__(self, arg):
        self.arg = arg

    def render(self, context):
        return self.code(self._full_path(context))

    @property
    def _cls_asc(self):
        return self.TAGS.get('cls_asc')

    @property
    def _cls_desc(self):
        return self.TAGS.get('cls_desc')

    @property
    def _cls_sort(self):
        return self.TAGS.get('cls_sort')

    @property
    def _a(self):
        return self.TAGS.get('a')

    def _full_path(self, context):
        self.reverse = bool(context.request.GET.get('reverse'))
        return context.request.get_full_path()

    def fa_class(self, full_path):
        order_str = 'order={0}'.format(self.arg)
        if order_str in full_path:
            fa_class = self._cls_asc if self.reverse else self._cls_desc
        else:
            fa_class = self._cls_sort
        return fa_class

    def add_sufix(self, full_path):
        if '?' not in full_path:
            full_path += '?'

        if 'order' not in full_path:
            full_path += '&order={0}'.format(self.arg)
        else:
            full_path = full_path.replace(
                self.util_path(full_path),
                'order={0}'.format(self.arg)
            )

        if 'reverse' not in full_path:
            full_path += '&reverse=True'
        else:
            full_path = full_path.replace('&reverse=True', '')

        return full_path

    def code(self, full_path):
        return self._a.format(
            path=self.add_sufix(full_path),
            fa_class=self.fa_class(full_path)
        )

    def util_path(self, full_path):
        list_item = full_path.split('&')
        for item in list_item:
            if 'order' in item:
                return item


@register.tag(name='order_by')
def order_by(parser, token):
    tag_name, arg = token.contents.split(None, 1)
    return OrderNode(arg)