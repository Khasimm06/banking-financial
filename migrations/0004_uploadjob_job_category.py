# Generated by Django 5.1.3 on 2025-01-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_uploadjob_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadjob',
            name='job_category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
