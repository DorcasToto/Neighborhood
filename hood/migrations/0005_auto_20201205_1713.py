# Generated by Django 3.1.3 on 2020-12-05 14:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_auto_20201205_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='photo', max_length=255, verbose_name='photo'),
        ),
    ]
