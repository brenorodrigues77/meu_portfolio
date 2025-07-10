from django.shortcuts import render
from portfolio.date import skills, projects


def home(request):
    return render(request, 'home.html', {'skills': skills})


def detail_project(request, project_id):
    project = projects.get(project_id)
    return render(request, 'detail_projects.html', {'project': project})
