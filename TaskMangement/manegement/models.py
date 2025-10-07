from datetime import date
from datetime import datetime
from django.db import models

# Create your models here.
class added_tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at_date = models.DateTimeField(default=date.today)
    created_at_time = models.TimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"

class in_progress_tasks(models.Model):
    name = models.CharField(max_length=200)
    created_at_date = models.DateTimeField()
    created_at_time = models.TimeField()
    description = models.TextField()
    in_progress_at_date = models.DateTimeField(default=date.today)
    in_progress_at_time = models.TimeField(default=datetime.now)
