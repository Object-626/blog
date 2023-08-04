from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Articles/', views.Articles, name='Articles'),
    path('author/', views.author, name='author'),
    path('create_author/', views.create_author, name='create_author'),
    path('<int:pk>', views.MainDetailView.as_view(), name='main-detail'),
    path('<int:pk>/update', views.MainUpdateView.as_view(), name='main-update'),
    path('<int:pk>/delete', views.MainDeleteView.as_view(), name='main-delete')
]
