from django.urls import path
from . import views


urlpatterns = [
    path('', views.HistoryListCreateAPIView.as_view()),
    path('id/<int:pk>', views.HistoryRetrieveUpdateAPIView.as_view()),
]
