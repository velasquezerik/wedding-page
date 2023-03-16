# Generated by Django 4.1.7 on 2023-03-16 08:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('short', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('n_people', models.IntegerField(default=1)),
                ('n_people_confirm', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='cards')),
            ],
        ),
    ]