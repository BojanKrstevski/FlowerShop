from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def home(request):
    articles = Article.objects.filter(author__username="bojan")
    # print(articles)
    return render(request, 'home.html', {'articles': articles})



def about(request):
    return render(request, 'about.html')
