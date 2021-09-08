# Generated by Django 3.2.7 on 2021-09-08 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0004_auto_20210908_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recording',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='recordings', to='music_publisher.artist', verbose_name='Recording Artist'),
        ),
        migrations.AlterField(
            model_name='release',
            name='recordings',
            field=models.ManyToManyField(related_name='recordings', through='music_publisher.Track', to='music_publisher.Recording'),
        ),
        migrations.AlterField(
            model_name='work',
            name='writers',
            field=models.ManyToManyField(related_name='works', through='music_publisher.WriterInWork', to='music_publisher.Writer'),
        ),
    ]
