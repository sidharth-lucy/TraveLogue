# Generated by Django 4.0.2 on 2022-07-29 17:15

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_userimage_aboutme_alter_userimage_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]