from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_picture = ProcessedImageField(
        blank=True,
        upload_to='profile/', 
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
    )