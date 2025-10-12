from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreatListView.as_view(), name='genre-creat-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
