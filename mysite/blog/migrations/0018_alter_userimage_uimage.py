# Generated by Django 4.0.2 on 2022-07-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_userimage_designation_userimage_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='uimage',
            field=models.ImageField(default='', upload_to='userimage'),
        ),
    ]
