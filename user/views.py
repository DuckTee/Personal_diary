from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from user.forms import UserRegisterForm
from user.models import User

class RegisterView(CreateView):
    """
    Регистрация пользователя
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'  # Исправлен путь
    success_url = reverse_lazy('diary:entry_list')  # Редирект в дневник

    def form_valid(self, form):
        user = form.save()  # Сохраняем пользователя
        login(self.request, user)  # Автовход
        return super().form_valid(form)  # Стандартный редирект на success_url

    def get_context_data(self, **kwargs):
        """Добавляем заголовок страницы в контекст."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
