# Generated by Django 3.2.13 on 2022-05-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm', '0014_alter_actualite_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='scan_1',
            field=models.ImageField(blank=True, null=True, upload_to='esm/static/img/inscriptions/'),
        ),
    ]