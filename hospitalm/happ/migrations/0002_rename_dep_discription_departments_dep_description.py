# Generated by Django 4.1.6 on 2023-10-29 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dep_discription',
            new_name='dep_description',
        ),
    ]
