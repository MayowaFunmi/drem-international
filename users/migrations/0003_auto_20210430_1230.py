# Generated by Django 3.1.5 on 2021-04-30 11:30

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210219_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/profile_pics/%Y/%m/%d/'), upload_to=''),
        ),
    ]
