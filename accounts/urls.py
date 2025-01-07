# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('my_account/', views.my_account, name='my_account'),
    path('logout/', views.logout_view, name='logout'),
]
