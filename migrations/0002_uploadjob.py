# Generated by Django 5.1.3 on 2025-01-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=100)),
                ('jobdescription', models.TextField()),
                ('joblocation', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('jobcreatedat', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='static/assets\\Jobs')),
                ('jobstatus', models.CharField(default='active', max_length=100)),
            ],
            options={
                'db_table': 'UploadJob',
            },
        ),
    ]
