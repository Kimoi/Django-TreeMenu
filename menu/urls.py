from django.urls import path

from .views import index, draw_menu_view

urlpatterns = [
    path('', index, name='main_menu'),
    path('<path:path>/', draw_menu_view, name='draw_menu_view'),
]
