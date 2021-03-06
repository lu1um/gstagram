from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import ArticleForm, CommentForm
from .models import Article, Picture, Comment


def index(request):
    if request.user.is_authenticated:
        articles = Article.objects.all()[::-1]
        comment_form = CommentForm()
        context = {
            'articles': articles,
            'comment_form':comment_form,
        }
        return render(request, 'articles/index.html', context)
    else:
        return redirect('accounts:login')


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
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


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'articles/profile.html', context)


def comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            article = get_object_or_404(Article, pk=pk)
            comment.article = article
            comment.save()
            return redirect('articles:index')