from django.conf import settings
from django.db import models
from django.utils import timezone


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
