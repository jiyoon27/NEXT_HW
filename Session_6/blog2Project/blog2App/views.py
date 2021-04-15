from django.shortcuts import render, redirect
from .models import Article
import time

# Create your views here.
def index(request):
    movie=Article.objects.filter(category="movie").count()
    drama=Article.objects.filter(category="drama").count()
    programming=Article.objects.filter(category="programming").count()
    return render(request, 'index.html', {'movie': movie, 'drama': drama, 'programming': programming})

def movie(request):
    movie_articles=Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'movie_articles': movie_articles})

def drama(request):
    drama_articles=Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'drama_articles': drama_articles})

def programming(request):
    programming_articles=Article.objects.filter(category="programming")
    return render(request, 'programming.html', {'programming_articles': programming_articles})

def detail(request, article_pk):
    article=Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title' ],
            content = request.POST['content' ],
            category = request.POST['category' ],
            time = time.ctime(time.time())
        )
        return redirect('detail', article_pk=new_article.pk)
    return render(request, 'new.html')

