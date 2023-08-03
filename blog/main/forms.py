from models import Author
from django.forms import ModelForm, TextInput


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'status', 'articles']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус'
            }),
            "articles": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статья'
            })
        }
