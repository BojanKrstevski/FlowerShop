from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def article_list(request):

    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    random = get_random_string(8, '0123456789')

    article = Article.objects.get(slug=slug)
    print(slug)
    return render(request, "articles/article_detail.html", {'article': article, 'random': random})


# def article_occasion(request, slug):
#     articles = Article.objects.filter(occasion=slug)
#     # return render(request, "articles/article_"+str(slug)+".html", {'articles': articles})
#     return render(request, "articles/article_.html", {'articles': articles})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request, "articles/article_create.html", {'form': form})


def article_birthday(request):
    articles = Article.objects.filter(occasion='birthday')
    print(articles)
    return render(request, 'articles/article_birthday.html', {'articles': articles})

def article_graduation(request):
    articles = Article.objects.filter(occasion='graduation')
    return render(request, "articles/article_graduation.html", {'articles': articles})

def article_anniversary(request):
    articles = Article.objects.filter(occasion='anniversary')
    return render(request, "articles/article_anniversary.html", {'articles': articles})

def article_getwell(request):
    articles = Article.objects.filter(occasion='getwell')
    return render(request, "articles/article_getwell.html", {'articles': articles})

def article_sympathy(request):
    articles = Article.objects.filter(occasion='sympathy')
    return render(request, "articles/article_sympathy.html", {'articles': articles})




