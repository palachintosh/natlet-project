# Generated by Django 2.2.10 on 2020-02-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]