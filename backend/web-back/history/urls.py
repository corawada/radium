from django.urls import path, include
from .views import ListHistory, DetailHistory

urlpatterns = [
    path('<int:pk>/', DetailHistory.as_view()),
    path('', ListHistory.as_view())
]
