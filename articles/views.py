from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from articles.models import Articles, Sections


class ArticlesSiteView(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'articles/articles.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticlesSiteView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        return context

    def get_queryset(self):
        queryset = super(ArticlesSiteView, self).get_queryset()
        section = self.request.GET.get('section')
        if section:
            self.template_name = 'articles/include/articles_list.html'
            if section != '0':
                queryset = Articles.objects.filter(sections=section)
        return queryset

