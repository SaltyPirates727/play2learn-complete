from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Associate review with the logged-in user
            review.save()
            return redirect('homepage')  # Redirect to homepage or wherever you want
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

