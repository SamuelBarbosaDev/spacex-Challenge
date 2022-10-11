# Generated by Django 4.1.2 on 2022-10-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_flickr_reddit_remove_patch_small_links_article_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='created',
        ),
        migrations.RemoveField(
            model_name='results',
            name='updated',
        ),
        migrations.AddField(
            model_name='results',
            name='auto_update',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='capsules_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='cores',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='crew_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='date_local',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='date_precision',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='date_unix',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='date_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='details',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='failures_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='flight_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='launch_library_id',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='launchpad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='net',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='payloads_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='rocket',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='ships_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='static_fire_date_unix',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='static_fire_date_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='success',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='tbd',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='upcoming',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='window',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
