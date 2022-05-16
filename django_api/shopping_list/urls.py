from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getAll', views.getAll),
    path('getById/<int:id>', views.getById),
    path('delete/<int:id>', views.delete),
    path('add', views.add),
]
