from django.forms import ModelForm

from .models import Photo


class ImageForm(ModelForm):
    """Form for the image model"""
    class Meta:
        model = Photo
        fields = ["image"]
