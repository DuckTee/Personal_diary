"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 1. Админ‑панель
    path("admin/", admin.site.urls),
    # 2. Аутентификация (стандартные URL: login, logout и др.)
    path("user/", include("django.contrib.auth.urls")),
    # 3. Кастомные URL для пользователя (регистрация и т.д.)
    path("user/", include("user.urls", namespace="user")),
    # 4. Основной функционал дневника (корневой URL)
    path("", include("diary.urls"), name="diary"),
]
