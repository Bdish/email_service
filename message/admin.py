from django.contrib import admin
from message.models import Message, Recipient, Error, ValueVariable


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Класс отображения отправленных сообщений."""

    list_display = (
        'id',
        'subject',
        'text',
        'id_template'
    )


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    """Список получателей."""

    list_display = (
        'id',
        'created',
        'send',
        'email',
        'id_message'
    )


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    """Список ошибок сообщения."""

    list_display = (
        'id',
        'id_message',
        'description'
    )


@admin.register(ValueVariable)
class ValueVariableAdmin(admin.ModelAdmin):
    """Список значений переменных."""

    list_display = (
        'id',
        'value',
        'id_message'
    )