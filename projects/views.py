from django.shortcuts import render

from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'detail.html', {'project': project})
