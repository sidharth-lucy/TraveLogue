# Generated by Django 4.0.2 on 2022-06-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_userimage_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='aboutme',
            field=models.TextField(),
        ),
    ]