# Generated by Django 2.2.10 on 2020-03-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0019_auto_20200301_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img_object',
            field=models.ImageField(db_index=True, upload_to='', verbose_name='Images'),
        ),
    ]