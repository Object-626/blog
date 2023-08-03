from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Articles/', views.index, name='Articles'),
    path('author/', views.index, name='author')
]
