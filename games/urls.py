from django.urls import path, include  # Add include here
from . import views
from games.views import MathFactsView, AnagramHuntView

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('contact-us/', include('contact.urls')),  # Add this line
]