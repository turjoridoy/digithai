from django.db import models
# Create your models here.
from django.utils import timezone


class Note(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
