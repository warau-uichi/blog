# Generated by Django 4.2.4 on 2023-08-21 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='uppdated_at',
        ),
    ]
