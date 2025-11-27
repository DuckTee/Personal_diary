from django.db import models
from user.models import User


class Entry(models.Model):
    """
    Модель записи
    """

    title = models.CharField(
        max_length=200, verbose_name="Заголовок", help_text="До 200 символов"
    )
    content = models.TextField(verbose_name="Содержание", help_text="Текст записи")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор", related_name="entries"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Запись дневника"
        verbose_name_plural = "Записи дневника"
        ordering = ["-created_at"]  # Новые записи сверху

    def __str__(self):
        return self.title
