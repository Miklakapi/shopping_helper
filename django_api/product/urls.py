from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('id/<int:pk>', views.ProductRetrieveUpdateAPIView.as_view()),
]
