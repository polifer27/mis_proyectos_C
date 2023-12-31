from django.http import Http404
from django.shortcuts import render, HttpResponse
#from requests import Response
#from .models import Project, FilesAdmin
from .models import Project
import os
from django.conf import settings

def portfolio(request):
    projects = Project.objects.all()
    #OUR_CONTEXT={'file':FilesAdmin.objects.all()}
    #file = FilesAdmin.objects.all()
    #return render(request, "core/portfolio.html", {'projects': projects, 'file':file})
    return render(request, "core/portfolio.html", {'projects': projects})

'''def home(request):
    # get all objects
    OUR_CONTEXT={'file':FilesAdmin.objects.all()}
    return render(request,'core/portfolio.html',OUR_CONTEXT)'''




def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404