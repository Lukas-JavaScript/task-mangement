from datetime import date, datetime
from django.db import models

def current_time():
    return datetime.now().time()
# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    created_at_date = models.DateField(default=date.today)
    created_at_time = models.TimeField(default=current_time)
