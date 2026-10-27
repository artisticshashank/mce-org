
from django.shortcuts import render, redirect
from .models import Project, Course
from .forms import ProjectForm


def index(request):
    courses = Course.objects.all()
    projects = Project.objects.all()

    return render(request, 'registration/index.html', {
        'courses': courses,
        'projects': projects,
    })


def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()

    return render(
        request,
        'registration/register_project.html',
        {'form': form}
    )
