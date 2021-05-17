"""Модуль создания моделей базы данных через ORM Django."""
from django.db import models


class Templates(models.Model):
    """Шаблон письма в формате html."""

    class Meta:
        db_table = 'templates'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, verbose_name='Название шаблона')
    description = models.TextField(blank=True, verbose_name='Полное описание шаблона')
    html = models.TextField(verbose_name='Шаблон в формате html с ключевыми словами в {}')

    def __str__(self):
        return f'{self.name}'


class BaseVariables(models.Model):
    """Список переменных, которые привязаны к шаблону и обязаны в шаблоне быть."""

    class Meta:
        db_table = 'base_variables'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, unique=True,
                            verbose_name='Название переменной в шаблоне, которое будет заключено в {}')
    description = models.TextField(blank=True, verbose_name='Описание назначения переменной')
    id_template = models.ForeignKey(Templates, null=True, on_delete=models.SET_NULL, to_field='id',
                                    db_column='id_template')

    def __str__(self):
        return f'{self.name}'






