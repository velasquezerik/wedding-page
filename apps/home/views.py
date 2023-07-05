from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import ImageForm

from .models import Photo

def index(request):
    all_entries = Photo.objects.all()
    paginator = Paginator(all_entries, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index2.html', {'photos': all_entries, "page_obj": page_obj})

def download(request, photo_id):
    document = get_object_or_404(Photo, pk=photo_id)
    response = HttpResponse(document.image, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{document.image.name}"'
    return response

def image_upload_view2(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'home/upload.html', {'form': form})

def image_upload_view(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Photo.objects.create(image=image)
    images = Photo.objects.all()
    return render(request, 'home/upload.html', {'images': images})