# Generated by Django 3.0.1 on 2020-08-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_works', '0002_studentsworks_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsworks',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='studentsworks',
            name='presentation',
            field=models.FileField(blank=True, null=True, upload_to='presentations/'),
        ),
    ]