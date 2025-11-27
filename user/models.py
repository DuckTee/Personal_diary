from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    Наследует все поля от AbstractUser.
    email — необязательное поле.
    """

    email = models.EmailField(
        verbose_name="Email", blank=True, null=True, help_text="Необязательно"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
