"""Модуль создания моделей базы данных через ORM Django."""
from django.db import models
from template.models import Templates


class Message(models.Model):
    """Отправляемое сообщение, его формат может быть един для нескольких получателей."""

    class Meta:
        db_table = "messages"

    id = models.AutoField(primary_key=True)
    subject = models.TextField(blank=True, verbose_name='Тема сообщения')
    text = models.TextField(blank=True, verbose_name='Текст сообщения', null=True)
    id_template = models.ForeignKey(Templates, null=True, on_delete=models.SET_NULL, to_field='id',
                                    db_column='id_template')


class Recipient(models.Model):
    """Получатель сообщения, с временем создания и отправки."""

    class Meta:
        db_table = "recipients"

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now=True, blank=True,  verbose_name='Время создания сообщения')
    send = models.DateTimeField(blank=True, verbose_name='Время отправки сообщения', null=True)
    email = models.CharField(max_length=254, verbose_name='Адрес электронной почты')
    id_message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL, to_field='id',
                                   db_column='id_message')


class ValueVariable(models.Model):
    """Значения переменных для конкретных писем."""

    class Meta:
        db_table = "value_variables"

    id = models.AutoField(primary_key=True)
    value = models.TextField(blank=True, verbose_name='Полное описание назначения переменной')
    id_message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL, to_field='id',
                                   db_column='id_message')


class Error(models.Model):
    """Описание ошибки связанное с отправкой."""

    class Meta:
        db_table = "errors"

    id = models.AutoField(primary_key=True)
    id_message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL, to_field='id',
                                   db_column='id_message')
    description = models.TextField(blank=True, verbose_name='Описание ошибки')