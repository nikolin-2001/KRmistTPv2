from django.db import models

class Operativka(models.Model):
    name = models.CharField('название оперативной памяти', max_length=200)
    price = models.CharField('Цена', max_length=200)
    pamyat = models.CharField('Память, гб', max_length=200)
    description = models.TextField('Описание', max_length=5000)
    def __str__(self):
        return self.name

class Videocard(models.Model):
    name = models.CharField('название видеокарты', max_length=200)
    price = models.CharField('Цена', max_length=200)
    pamyat = models.CharField('Память', max_length=200)
    mochnost = models.CharField('Мощность', max_length=200)
    description = models.TextField('Описание', max_length=5000)
