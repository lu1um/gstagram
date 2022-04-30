# Generated by Django 3.2.12 on 2022-04-30 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20220429_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
