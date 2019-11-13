from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='users-dashboard'),
    path('register/', views.register, name='users-register'),
    path('profile/', views.profile, name='users-profile'),
]