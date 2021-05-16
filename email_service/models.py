"""Модуль создания моделей базы данных через ORM Django."""
from django.db import models


class Templates(models.Model):
    """Шаблон письма в формате html."""

    class Meta:
        db_table = "templates"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, verbose_name='Название шаблона')
    description = models.TextField(blank=True, verbose_name='Полное описание шаблона')
    html = models.TextField(verbose_name='Шаблон в формате html с ключевыми словами в {}')


class BaseVariables(models.Model):
    """Список переменных, которые привязаны к шаблону и обязаны в шаблоне быть."""

    class Meta:
        db_table = "base_variables"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, unique=True,
                            verbose_name='Название переменной в шаблоне, которое будет заключено в {}')
    description = models.TextField(blank=True, verbose_name='Описание назначения переменной')
    id_template = models.ForeignKey(Templates, null=True, on_delete=models.SET_NULL, to_field='id',
                                    db_column='id_template')


class Messages(models.Model):
    """Отправляемое сообщение, его формат может быть един для нескольких получателей."""

    class Meta:
        db_table = "messages"

    id = models.IntegerField(primary_key=True)
    id_template = models.ForeignKey(Templates, null=True, on_delete=models.SET_NULL, to_field='id',
                                    db_column='id_template')


class Recipients(models.Model):
    """Получатель сообщения, с временем создания и отправки."""

    class Meta:
        db_table = "recipients"

    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now=True, blank=True,  verbose_name='Время создания сообщения')
    send = models.DateTimeField(blank=True, verbose_name='Время отправки сообщения')
    email = models.CharField(max_length=254, verbose_name='Адрес электронной почты')
    id_message = models.ForeignKey(Messages, null=True, on_delete=models.SET_NULL, to_field='id',
                                   db_column='id_message')


class ValueVariables(models.Model):
    """Значения переменных для конкретных писем."""

    class Meta:
        db_table = "value_variables"

    id = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True, verbose_name='Полное описание назначения переменной')
    id_message = models.ForeignKey(Messages, null=True, on_delete=models.SET_NULL, to_field='id',
                                   db_column='id_message')
