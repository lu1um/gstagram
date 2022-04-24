from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article, Picture


def index(request):
    if request.user.is_authenticated:
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index.html', context)
    else:
        return redirect('accounts:login')


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            picture = Picture()
            picture.article = article
            picture.upload_picture = form.cleaned_data.get('picture')
            picture.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)