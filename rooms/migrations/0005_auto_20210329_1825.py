# Generated by Django 2.2.5 on 2021-03-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210323_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bedsrooms',
            new_name='bedrooms',
        ),
    ]
