# Generated by Django 3.2.13 on 2022-04-13 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm', '0004_inscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='esm/static/img/inscriptions/<django.db.models.fields.CharField>-<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_1',
            field=models.ImageField(upload_to='esm/static/img/inscriptions/<django.db.models.fields.CharField>-<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_2',
            field=models.ImageField(blank=True, null=True, upload_to='esm/static/img/inscriptions/<django.db.models.fields.CharField>-<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_3',
            field=models.ImageField(blank=True, null=True, upload_to='esm/static/img/inscriptions/<django.db.models.fields.CharField>-<django.db.models.fields.CharField>/'),
        ),
    ]