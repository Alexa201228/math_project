# Generated by Django 3.0.1 on 2020-08-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsworks',
            name='source',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
