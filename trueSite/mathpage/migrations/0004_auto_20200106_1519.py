# Generated by Django 3.0.1 on 2020-01-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathpage', '0003_auto_20200106_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathpage',
            name='image',
            field=models.ImageField(null=True, upload_to='math_images/'),
        ),
    ]
