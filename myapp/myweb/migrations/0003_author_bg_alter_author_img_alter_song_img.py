# Generated by Django 5.0.6 on 2024-09-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_author_playlist_description_playlist_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bg',
            field=models.CharField(default='default_background_image', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]
