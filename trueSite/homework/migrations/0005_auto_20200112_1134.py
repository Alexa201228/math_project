# Generated by Django 3.0.1 on 2020-01-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_remove_homework_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='homework_images'),
        ),
    ]