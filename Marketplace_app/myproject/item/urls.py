from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('item/<int:pk>/', views.detail, name='detail'),
    path('item/new/', views.create, name='create'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),
    path('item/<int:pk>/edit/', views.edit, name='edit'),
    path('', views.items, name='items'),
]