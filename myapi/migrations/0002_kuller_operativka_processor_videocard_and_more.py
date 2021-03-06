# Generated by Django 4.0.1 on 2022-01-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kuller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название комплектующих')),
                ('image', models.TextField(max_length=5000, verbose_name='URL изоображения')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('mochnost', models.CharField(max_length=200, verbose_name='Мощность')),
            ],
        ),
        migrations.CreateModel(
            name='Operativka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название комплектующих')),
                ('image', models.TextField(max_length=5000, verbose_name='URL изоображения')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
                ('pamyat', models.CharField(max_length=200, verbose_name='Память')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название комплектующих')),
                ('image', models.TextField(max_length=5000, verbose_name='URL изоображения')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('mochnost', models.CharField(max_length=200, verbose_name='Мощность')),
            ],
        ),
        migrations.CreateModel(
            name='Videocard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название комплектующих')),
                ('image', models.TextField(max_length=5000, verbose_name='URL изоображения')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
                ('pamyat', models.CharField(max_length=200, verbose_name='Память')),
                ('mochnost', models.CharField(max_length=200, verbose_name='Мощность')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.DeleteModel(
            name='PK',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
