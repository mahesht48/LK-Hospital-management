# Generated by Django 4.1.6 on 2023-10-29 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0004_alter_doctors_doc_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='doc_image',
        ),
    ]
