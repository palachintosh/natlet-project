# Generated by Django 2.2.10 on 2020-03-02 08:16

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0021_auto_20200302_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img_object',
            field=models.ImageField(db_index=True, storage=django.core.files.storage.FileSystemStorage(location='default/location/'), upload_to='', verbose_name='Images'),
        ),
    ]
