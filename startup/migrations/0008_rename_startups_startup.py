# Generated by Django 4.0.3 on 2022-04-10 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_investor_delete_startupper'),
        ('startup', '0007_delete_startup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Startups',
            new_name='Startup',
        ),
    ]
