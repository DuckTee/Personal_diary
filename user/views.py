from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import (LoginView,  # ← правильный импорт
                                       LogoutView)
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserRegisterForm
from user.models import User


class RegisterView(CreateView):
    """
    Регистрация пользователя
    """

    model = User
    form_class = UserRegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("diary:entry_list")

    def form_valid(self, form):
        user = form.save()  # Сохраняем пользователя
        login(self.request, user)  # Автовход
        messages.success(
            self.request, "Регистрация прошла успешно! Вы вошли в систему."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка при регистрации. Проверьте данные.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        """Добавляем заголовок страницы в контекст."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context


class LoginViewCustom(LoginView):
    """
    Кастомное представление для входа
    """

    template_name = "registration/login.html"
    success_url = reverse_lazy("diary:entry_list")

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно вошли в систему.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверные логин или пароль.")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutViewCustom(LogoutView):
    next_page = None  # По умолчанию нет редиректа

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы вышли из системы.")
        return super().dispatch(request, *args, **kwargs)
