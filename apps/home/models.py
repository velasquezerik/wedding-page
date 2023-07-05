import uuid

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images', blank=True)
    image_resize = ImageSpecField(source='image',
                                      processors=[ResizeToFill(800, 600)],
                                      format='JPEG',
                                      options={'quality': 60})
