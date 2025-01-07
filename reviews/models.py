from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Date when the review was submitted
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at}"

