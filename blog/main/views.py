from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.views.generic import DeleteView, UpdateView, DetailView
from .models import Author

def index(request):
    return render(request, 'main/index.html')


def Articles(request):
    return render(request, 'main/Articles.html')


def author(request):
    authors = Author.objects.all()
    return render(request, 'main/author.html', {'authors': authors})


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


class MainDeleteView(DeleteView):
    model = Author
    success = '/main/'
    template_name = 'main/delete.html'


class MainUpdateView(UpdateView):
    model = Author
    template_name = 'main/create_author.html'
    form_class = AuthorForm


class MainDetailView(DetailView):
    model = Author
    template_name = 'main/details_view.html'
    context_object_name = 'author'


