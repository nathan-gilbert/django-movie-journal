from django.forms import ModelForm

from .models import MovieJournalEntry


class NewEntryForm(ModelForm):
    """
    This form is used to create a new MovieJournalEntry.
    """

    class Meta:
        model = MovieJournalEntry
        fields = ("title", "imdb_link", "is_positive", "review", "release_year")
