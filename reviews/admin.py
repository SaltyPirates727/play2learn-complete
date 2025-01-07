from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    # Define which fields you want to display in the admin list view
    list_display = ('user', 'created_at', 'review_text', 'featured')

    # Optional: Add search fields for easier navigation
    search_fields = ('user__username', 'review_text')

    # Optional: Add filters for easy filtering by user or featured status
    list_filter = ('featured', 'user')

    # Optional: Set the default ordering of reviews by date submitted
    ordering = ('-created_at',)  # Display most recent reviews first

admin.site.register(Review, ReviewAdmin)
