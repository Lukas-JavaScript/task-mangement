from django.shortcuts import render

# Create your views here.
def comments(request):
    return render(request, 'index.html')
