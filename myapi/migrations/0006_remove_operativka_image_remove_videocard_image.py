# Generated by Django 4.0.1 on 2022-01-15 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_operativka_name_alter_videocard_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operativka',
            name='image',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='image',
        ),
    ]