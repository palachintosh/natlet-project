# Generated by Django 2.2.10 on 2020-02-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0012_auto_20200229_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img_object',
            field=models.ImageField(db_index=True, upload_to=None, verbose_name='Images'),
        ),
    ]
