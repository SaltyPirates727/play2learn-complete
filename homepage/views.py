from django.shortcuts import render
from reviews.models import Review

def homepage(request):
    # Get featured reviews
    featured_reviews = Review.objects.filter(featured=True)

    # Render the homepage with featured reviews
    return render(request, 'homepage/homepage.html', {'featured_reviews': featured_reviews})
