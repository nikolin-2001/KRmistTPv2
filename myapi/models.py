from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

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
