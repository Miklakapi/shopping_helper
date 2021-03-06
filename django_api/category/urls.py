from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view()),
    path('no-pagination', views.CategoryListAPIView.as_view()),
    path('id/<int:pk>', views.CategoryRetrieveUpdateAPIView.as_view()),
]
