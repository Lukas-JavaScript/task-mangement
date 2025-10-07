from datetime import date, datetime
from django.db import models


def current_time():
    return datetime.now().time()
# Create your models here.
class added_tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at_date = models.DateField(default=date.today)
    created_at_time = models.TimeField(default=current_time)

    def __str__(self):
        return f"{self.name}"

class in_progress_tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at_date = models.DateField()
    created_at_time = models.TimeField()
    in_progress_at_date = models.DateField(default=date.today)
    in_progress_at_time = models.TimeField(default=current_time)

    def __str__(self):
        return f"{self.name}"

class completed_tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at_date = models.DateField()
    created_at_time = models.TimeField()
    in_progress_at_date = models.DateField()
    in_progress_at_time = models.TimeField()
    completed_at_date = models.DateField(default=date.today)
    completed_at_time = models.TimeField(default=current_time)

    def __str__(self):
        return f"{self.name}"
