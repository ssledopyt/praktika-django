from django.urls import path, include

from .views import TestView, TestPlayView

urlpatterns = [
    path('', TestView.as_view()),
    path('', TestPlayView.as_view())
]