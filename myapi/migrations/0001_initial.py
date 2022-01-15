# Generated by Django 4.0.1 on 2022-01-15 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название комплектующих')),
                ('image', models.TextField(max_length=5000, verbose_name='URL изоображения')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('displei', models.CharField(max_length=200, verbose_name='Дисплей')),
                ('processor', models.CharField(max_length=200, verbose_name='Процессор')),
                ('operativka', models.CharField(max_length=200, verbose_name='Оперативка')),
                ('nakopiteli', models.CharField(max_length=200, verbose_name='Накопитель')),
                ('ves', models.CharField(max_length=200, verbose_name='Вес')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.pk')),
            ],
        ),
    ]