from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as SuperUserCreationForm


class UserCreationForm(SuperUserCreationForm):

    class Meta(SuperUserCreationForm.Meta):
        model = get_user_model()
        fields = SuperUserCreationForm.Meta.fields