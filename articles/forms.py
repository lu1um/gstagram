from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    picture = forms.ImageField()
    class Meta:
        model = Article
        fields = ('content', 'picture',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', )
    class Meta:
        model = Comment
        fields = ('content',)