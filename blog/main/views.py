from django.shortcuts import render
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
        form = AuthorForm()
