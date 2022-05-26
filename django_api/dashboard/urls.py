from django.urls import path
from . import views


urlpatterns = [
    path('spends', views.SpendsListAPIView.as_view()),
    path('spends-by-month-chart', views.SpendsByMonthChartListAPIVIew.as_view())
]
