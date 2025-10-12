from datetime import date, datetime
from django.db import models

def current_time():
    return datetime.now().time()
# Create your models here.
class Comment(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at_date = models.DateField(default=date.today)
    created_at_time = models.TimeField(default=current_time)
    def __str__(self):
        return self.subject
