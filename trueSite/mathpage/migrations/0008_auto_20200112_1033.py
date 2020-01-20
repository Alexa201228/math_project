# Generated by Django 3.0.1 on 2020-01-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathpage', '0007_remove_mathpage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathpage',
            name='image_solution',
            field=models.ImageField(default=None, null=True, upload_to='math_images/'),
        ),
        migrations.AlterField(
            model_name='mathpage',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='mathpage',
            name='solution',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='mathpage',
            name='title',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]