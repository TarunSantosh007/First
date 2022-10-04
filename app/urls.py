from django.urls import path
from .import views

urlpatterns = [

    path('movie-data', views.movieData, name = 'movie-data'),
    path('movie-create', views.movieCreate, name = 'movie-create'),
    path('movie-update/<str:pk>/', views.movieUpdate, name = 'movie-update'),
    path('movie-delete/<str:pk>/', views.movieDelete, name = 'movie-delete'),

]