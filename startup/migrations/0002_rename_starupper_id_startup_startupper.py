# Generated by Django 4.0.3 on 2022-03-07 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='starupper_id',
            new_name='startupper',
        ),
    ]