# Generated by Django 2.2.6 on 2019-10-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='amount',
            new_name='phone',
        ),
    ]
