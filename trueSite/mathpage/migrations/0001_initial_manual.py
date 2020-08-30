# Generated by Django 3.0.1 on 2020-08-26 12:24

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
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('theme', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='math_images/')),
                ('description', models.TextField(blank=True, default='')),
                ('solution', models.TextField(blank=True, default='')),
                ('slug', models.SlugField(default='', max_length=250)),
                ('image_solution', models.ImageField(blank=True, null=True, upload_to='math_images/')),
            ],
        ),
    ]
