# Generated by Django 3.0.1 on 2019-12-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='math_images/')),
                ('little_summary', models.CharField(max_length=300)),
            ],
        ),
    ]