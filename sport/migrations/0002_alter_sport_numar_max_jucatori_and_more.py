# Generated by Django 4.0.4 on 2022-05-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='numar_max_jucatori',
            field=models.IntegerField(verbose_name=3),
        ),
        migrations.AlterField(
            model_name='sport',
            name='numar_min_jucatori',
            field=models.IntegerField(verbose_name=2),
        ),
    ]