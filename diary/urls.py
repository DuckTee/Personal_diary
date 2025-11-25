from django.urls import path
from . import views
from .views import HomeView

app_name = 'diary'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # Главная страница
    path("entries/", views.EntryListView.as_view(), name='entry_list'),
    path('create/', views.EntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/edit/', views.EntryUpdateView.as_view(), name='entry_edit'),
    path('<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
    path('<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
]

