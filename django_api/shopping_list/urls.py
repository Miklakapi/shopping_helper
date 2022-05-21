from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShoppingListCreateAPIView.as_view()),
    path('id/<int:pk>', views.ShoppingListRetrieveDestroyAPIView.as_view()),
]
