# Generated by Django 3.2.13 on 2022-05-13 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esm', '0021_remove_inscription_athlete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='esm.groupe'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]