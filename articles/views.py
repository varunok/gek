from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView

from articles.models import Articles, Sections
from common.mixins import ViewsCountMixin
from seo.mixins import SEOMixin

PAGINATE_ARTICLE = 10


class ArticlesSiteView(SEOMixin, ListView):
    model = Articles
    context_object_name = 'objects'
    template_name = 'articles/articles.html'
    dinamic_template_name = 'articles/include/articles_list.html'
    paginate_by = PAGINATE_ARTICLE

    def get_context_data(self, **kwargs):
        context = super(ArticlesSiteView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        return context


class SectionsDetailView(SEOMixin, DetailView):
    model = Sections
    slug_field = 'slug'
    context_object_name = 'section'
    template_name = 'articles/sections.html'

    def get_context_data(self, **kwargs):
        context = super(SectionsDetailView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        context['article_count'] = Articles.objects.count()
        try:
            context['articles'] = Articles.objects.filter(sections=self.object)[:PAGINATE_ARTICLE]
            count_next = Articles.objects.filter(sections=self.object).count() - PAGINATE_ARTICLE
            context['count_next'] = 0 if count_next <= 0 else count_next
        except:
            pass
        print(context['articles'])
        return context


class ArticlesDetailView(SEOMixin, ViewsCountMixin, DetailView):
    model = Articles
    slug_url_kwarg = 'slug_a'
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        context['article_count'] = Articles.objects.count()
        return context
