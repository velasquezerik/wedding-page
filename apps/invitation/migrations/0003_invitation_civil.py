# Generated by Django 4.1.7 on 2023-03-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='civil',
            field=models.BooleanField(default=False),
        ),
    ]