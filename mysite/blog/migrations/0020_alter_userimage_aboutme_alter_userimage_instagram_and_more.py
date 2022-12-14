# Generated by Django 4.0.2 on 2022-07-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_userimage_uimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='aboutme',
            field=models.TextField(default='Please Write somthing about yourself.', max_length=1300),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='instagram',
            field=models.URLField(default='https://www.instagram.com/', max_length=300),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='twiter',
            field=models.URLField(default='https://twitter.com/', max_length=300),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='youtube',
            field=models.URLField(default='https://www.youtube.com/', max_length=300),
        ),
    ]
