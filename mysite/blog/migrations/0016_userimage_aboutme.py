# Generated by Django 4.0.2 on 2022-06-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_userimage_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='aboutme',
            field=models.TextField(default='Please Write somthing about yourself.'),
        ),
    ]
