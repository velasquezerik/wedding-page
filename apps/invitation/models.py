import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return str(self.name) + ' ' + str(self.id)


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)
    short = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    n_people = models.IntegerField(default=1)
    n_people_confirm = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    not_coming = models.BooleanField(default=False)
    civil = models.BooleanField(default=False)
    image = models.ImageField(upload_to='cards', blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.id) + ' : Confimacion - ' + str(self.status)
