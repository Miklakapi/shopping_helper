from django.urls import path

from .views import LoginView, isLoginView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('isLogin', isLoginView.as_view())
]
