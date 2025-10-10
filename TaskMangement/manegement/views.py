from django.shortcuts import render
from .models import added_tasks, in_progress_tasks, completed_tasks
from .fn import add_task, set_in_progress

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST.get('subject') == 'add':
            headline = request.POST.get('headline')
            description = request.POST.get('description')
            add_task(headline, description)
        if request.POST.get('subject') == 'set_in_progress':
            task_id = request.POST.get('id')
            set_in_progress(task_id)
    added = added_tasks.objects.all()
    in_progress = in_progress_tasks.objects.all()
    completed = completed_tasks.objects.all()
    return render(request, 'index.html', {
        'added_tasks': added,
        'in_progress_tasks': in_progress,
        'completed_tasks': completed,
    })
