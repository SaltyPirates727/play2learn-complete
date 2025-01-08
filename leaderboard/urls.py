from django.urls import path
from . import views

urlpatterns = [
    path('submit-score/', views.submit_score, name='submit_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/', views.leaderboard_json, name='leaderboard_json'),  # Endpoint for JSON leaderboard
]
