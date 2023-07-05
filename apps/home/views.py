from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Photo

def index(request):
    all_entries = Photo.objects.all()
    paginator = Paginator(all_entries, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index2.html', {'photos': all_entries, "page_obj": page_obj})

def download(request, photo_id):
    document = get_object_or_404(Photo, pk=photo_id)
    response = HttpResponse(document.image, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{document.image.name}"'
    return response