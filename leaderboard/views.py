from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.shortcuts import render
from .models import LeaderboardEntry
import json

@csrf_exempt
def submit_score(request):
    if request.method == "GET":
        # Get username from the authenticated user, or fallback to "Anonymous"
        username = request.user.username if request.user.is_authenticated else "Anonymous"
        score = request.GET.get("score", 0)
        game_type = request.GET.get("game_type", "Unknown")

        # Save the score to the database
        entry = LeaderboardEntry.objects.create(
            username=username, score=score, game_type=game_type
        )
        return JsonResponse({"message": "Score submitted successfully", "entry_id": entry.id}, status=201)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def leaderboard(request):
    # Retrieve the top 10 leaderboard entries ordered by score and date
    leaderboard_entries = LeaderboardEntry.objects.order_by('-score', '-date_submitted')[:10]
    context = {'leaderboard_entries': leaderboard_entries}
    return render(request, 'leaderboard/leaderboard.html', context)


def leaderboard_json(request):
    # Return leaderboard data in JSON format
    leaderboard_entries = LeaderboardEntry.objects.order_by('-score', '-date_submitted')
    data = {
        'leaderboard': [
            {
                'username': entry.username,
                'score': entry.score,
                'game_type': entry.game_type,
                'date_submitted': entry.date_submitted.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for entry in leaderboard_entries
        ]
    }
    return JsonResponse(data)
