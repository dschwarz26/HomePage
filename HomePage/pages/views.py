from django.shortcuts import render, get_object_or_404
from HomePage.pages.models import Essay, Biopic, Personal, Project, Link

def home(request):
    context = {
        'essays': Essay.objects.all().order_by('rank'),
        'biopics': Biopic.objects.all().order_by('rank'),
        'personals': Personal.objects.all().order_by('rank'),
        'projects': Project.objects.all().order_by('rank'),
        'links': Link.objects.all().order_by('rank')
    }
    return render(request, 'home.html', context)

def resume(request):
    return render(request, 'resume.html')

def essay(request, essay_name):
    essay = get_object_or_404(Essay, pk = essay_name)
    return render(request, 'essay.html', {'essay': essay})

def biopic(request, biopic_name):
    biopic = get_object_or_404(Biopic, pk = biopic_name)
    return render(request, 'biopic.html', {'biopic': biopic})

def personal(request, personal_name):
    personal = get_object_or_404(Personal, pk = personal_name)
    return render(request, 'personal.html', {'personal': personal})