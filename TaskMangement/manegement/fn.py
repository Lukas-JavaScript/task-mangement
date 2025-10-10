from .models import added_tasks, in_progress_tasks, completed_tasks, removed_tasks


def add_task(headline, description):
    print(f"Adding task: {headline} with description: {description}")
    added_tasks.objects.create(name=headline, description=description)


def set_in_progress(task_id):
    task = added_tasks.objects.get(id=task_id)
    in_progress_tasks.objects.create(name=task.name,
                                      description=task.description,
                                      created_at_date=task.created_at_date,
                                      created_at_time=task.created_at_time)
    added_tasks.objects.get(id=task_id).delete()
