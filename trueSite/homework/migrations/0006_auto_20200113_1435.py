# Generated by Django 3.0.1 on 2020-01-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_auto_20200112_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
