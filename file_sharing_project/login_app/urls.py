from django.urls import path, include
from django.contrib.auth import views as auth_views
from login_app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # Add more URLs as needed
]