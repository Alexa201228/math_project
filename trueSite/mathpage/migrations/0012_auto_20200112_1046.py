# Generated by Django 3.0.1 on 2020-01-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathpage', '0011_auto_20200112_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathpage',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
