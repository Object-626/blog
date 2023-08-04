from django.shortcuts import render, redirect
from .forms import AuthorForm


def index(request):
    return render(request, 'main/index.html')


def Articles(request):
    return render(request, 'main/Articles.html')


def author(request):
    return render(request, 'main/author.html')


def create_author(request):
    error = ''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неверно'

    form = AuthorForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_author.html', data)
