# Generated by Django 4.0.2 on 2022-06-18 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_userimage_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='aboutme',
        ),
    ]
