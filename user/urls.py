from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # Страница входа
    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),

    # Регистрация
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ),

    # Выход из аккаунта
    path(
        'logout/',
        LogoutView.as_view(
            template_name='diary/logged_out.html',
        ),
        name='logout'
    ),
]
