# Generated by Django 3.0.1 on 2020-08-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathpage', '0002_auto_20200826_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathpage',
            name='fileSolution',
            field=models.FileField(blank=True, upload_to='math_materials/'),
        ),
    ]