# Generated by Django 3.2.13 on 2022-05-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm', '0031_remove_inscription_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='emploi',
            field=models.ImageField(blank=True, null=True, upload_to='emplois-du-temps/'),
        ),
    ]
