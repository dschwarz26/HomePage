from django.shortcuts import render, get_object_or_404
from HomePage.pages.models import Essay

def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def essay(request, essay_id):
    essay = get_object_or_404(Essay, pk = essay_id)
    return render(request, 'essay.html', {'essay': essay})