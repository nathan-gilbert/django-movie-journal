from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import NewEntryForm
from .models import MovieJournalEntry


def index(request):
    journal_entries = MovieJournalEntry.objects.order_by("-created_at")
    context = {
        "journal_entries": journal_entries,
    }
    return render(request, "index.html", context)


def new(request):
    EntryForm = modelform_factory(MovieJournalEntry, form=NewEntryForm)

    if request.method == "POST":
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect("detail", entry_id=instance.id)
    else:
        form = EntryForm()

    return render(request, "new.html", {"form": form})


def detail(request, entry_id):
    try:
        entry = MovieJournalEntry.objects.get(pk=entry_id)
    except MovieJournalEntry.DoesNotExist:
        raise Http404("MovieJournalEntry does not exist")
    return render(request, "detail.html", {"entry": entry})
