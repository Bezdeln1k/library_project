from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UploadXMLForm

def upload_xml(request):
    if request.method == 'POST':
        form = UploadXMLForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('upload-xml'))
    else:
        form = UploadXMLForm()
    return render(request, 'upload_xml.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.xml', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)