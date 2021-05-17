from django.contrib import admin
from template.models import Templates, BaseVariables


@admin.register(Templates)
class TemplatesAdmin(admin.ModelAdmin):
    """Класс нрастройки html шаблона email сообщения."""

    list_display = (
        'name',
        'description',
        'html'
    )


@admin.register(BaseVariables)
class BaseVariablesAdmin(admin.ModelAdmin):
    """Класс добавления ключевых переменных для шаблона."""

    list_display = (
        'name',
        'description'
    )



