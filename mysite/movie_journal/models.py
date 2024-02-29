from django.db import models


class MovieJournalEntry(models.Model):
    title = models.CharField(max_length=300)
    imdb_link = models.URLField()
    is_positive = models.BooleanField()
    review = models.TextField()
    release_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
