# Generated by Django 3.0.1 on 2019-12-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20191227_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
