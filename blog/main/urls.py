from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Articles/', views.Articles, name='Articles'),
    path('author/', views.author, name='author'),
    path('create_author/', views.create_author, name='create_author')
]
