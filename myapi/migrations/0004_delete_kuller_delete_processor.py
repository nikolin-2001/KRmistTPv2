# Generated by Django 4.0.1 on 2022-01-15 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_operativka_pamyat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kuller',
        ),
        migrations.DeleteModel(
            name='Processor',
        ),
    ]
