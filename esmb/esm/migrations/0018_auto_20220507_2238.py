# Generated by Django 3.2.13 on 2022-05-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm', '0017_auto_20220507_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='inscriptions/photos/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_1',
            field=models.ImageField(upload_to='inscriptions/scans/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_2',
            field=models.ImageField(blank=True, null=True, upload_to='inscriptions/scans/'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scan_3',
            field=models.ImageField(blank=True, null=True, upload_to='inscriptions/scans/'),
        ),
    ]
