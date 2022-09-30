# Generated by Django 4.0.2 on 2022-09-14 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_post_follower_post_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='post',
            name='following',
        ),
        migrations.AddField(
            model_name='userimage',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userimage',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
