# Generated by Django 3.0.1 on 2020-01-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_auto_20200113_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='theme',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
