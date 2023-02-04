from django.db import models


class Case(models.Model):
    uuid = models.CharField(verbose_name='uuid', max_length=8, unique=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    body = models.TextField(verbose_name='Текст', max_length=2000)
    active = models.BooleanField(default=True)
