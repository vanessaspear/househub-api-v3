# Generated by Django 4.2 on 2023-04-25 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('househubapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flooringtype',
            old_name='flooring_type',
            new_name='type',
        ),
    ]
