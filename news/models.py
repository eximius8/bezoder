from django.db import models
from person.models import NewsAuthor

class NewsItem(models.Model):
    headline = models.CharField(max_length=150)
    datepublished = models.DateField(auto_now=True)
    newstext = models.TextField()
    newsauthor = models.ForeignKey(NewsAuthor, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
