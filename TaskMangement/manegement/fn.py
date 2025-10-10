from .models import added_tasks, in_progress_tasks, completed_tasks, removed_tasks

def add_task(headline, description):
    print(f"Adding task: {headline} with description: {description}")
    added_tasks.objects.create(name=headline, description=description)
