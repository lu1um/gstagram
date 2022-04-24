from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.method == 'POST':
        pass
    else:
        pass
    context = {

    }
    return render(request, 'accounts/signup.html', context)
