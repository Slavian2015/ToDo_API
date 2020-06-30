from django.db import models
from django.utils.timezone import now

# Create your models here.
class Todo(models.Model):
    date = models.DateTimeField(default=now, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title