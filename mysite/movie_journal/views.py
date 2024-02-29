from django.http import Http404
from django.shortcuts import render

from .models import MovieJournalEntry


def index(request):
    journal_entries = MovieJournalEntry.objects.order_by("-created_at")
    context = {
        "journal_entries": journal_entries,
    }
    return render(request, "index.html", context)


def detail(request, question_id):
    try:
        entry = MovieJournalEntry.objects.get(pk=question_id)
    except MovieJournalEntry.DoesNotExist:
        raise Http404("MovieJournalEntry does not exist")
    return render(request, "detail.html", {"entry": entry})
