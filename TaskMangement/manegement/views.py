from django.shortcuts import render
from .models import added_tasks, in_progress_tasks, completed_tasks, removed_tasks


# Create your views here.
def home(request):
    added = added_tasks.objects.all()
    in_progress = in_progress_tasks.objects.all()
    completed = completed_tasks.objects.all()

    return render(request, 'index.html', {
        'added_tasks': added,
        'in_progress_tasks': in_progress,
        'completed_tasks': completed,
    })
