# Generated by Django 4.0.4 on 2022-05-27 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_alter_sport_numar_max_jucatori_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='description',
            new_name='descriere',
        ),
    ]
