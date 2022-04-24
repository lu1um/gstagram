from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm as SuperUserCreationForm


class UserCreationForm(SuperUserCreationForm):

    class Meta(SuperUserCreationForm):
        model = settings.AUTH_USER_MODEL
        fields = SuperUserCreationForm.fields