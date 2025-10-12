from django.shortcuts import render
from .models import Comment

# Create your views here.
def comments(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        Comment.objects.create(subject=subject, description=description)
    return render(request, 'comments.html', {'comments': comments})
