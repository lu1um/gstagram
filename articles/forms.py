from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    picture = forms.ImageField()
    class Meta:
        model = Article
        fields = '__all__'