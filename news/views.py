from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    # print(dir(request))
    news = News.objects.all()  # order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})
