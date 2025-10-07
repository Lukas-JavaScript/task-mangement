from django.contrib import admin
from .models import added_tasks, in_progress_tasks, completed_tasks

# Register your models here.
admin.site.register(added_tasks)
admin.site.register(in_progress_tasks)
admin.site.register(completed_tasks)
