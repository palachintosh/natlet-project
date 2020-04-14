# Generated by Django 2.2.10 on 2020-03-30 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novatlet', '0031_auto_20200327_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.CharField(db_index=True, max_length=700)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment_for_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='novatlet.Post')),
            ],
        ),
    ]