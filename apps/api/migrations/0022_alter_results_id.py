# Generated by Django 4.1.2 on 2022-10-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_results_iid_alter_results_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]