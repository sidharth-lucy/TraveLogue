# Generated by Django 4.0.2 on 2022-07-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_userimage_uimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='uimage',
            field=models.ImageField(default=None, upload_to='userimage'),
        ),
    ]