from .models import added_tasks, in_progress_tasks, completed_tasks, removed_tasks

def add_task(name, description):
    added_tasks.objects.create(name=name, description=description)
