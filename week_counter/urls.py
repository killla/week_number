from django.urls import path
from . import views


urlpatterns = [
    path('week/', views.process_dates),
]
