from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoriesListCreateAPIView.as_view()),
    path('id/<int:pk>', views.CategoriesRetrieveDestroyAPIView.as_view()),
]
