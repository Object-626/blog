from django.db import models


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)
    status = models.CharField('Статус', max_length=100)
    #photo = models.ImageField('Фото автора', upload_to="author/")
    articles = models.CharField('Статья', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

