from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    return render(request, "core/portfolio.html", {'projects': projects})