from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list_create, name='user_list'),
    path('edit/<int:pk>/', views.user_update, name='user_edit'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
]