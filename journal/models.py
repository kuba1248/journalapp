from django.db import models
from django.urls import reverse


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
