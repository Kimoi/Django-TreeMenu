from django.shortcuts import render

from .models import Menu


def index(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def draw_menu_view(request, path):
    slashed_path = path.split('/')
    return render(request, 'menu/index.html', {'menu_name': slashed_path[0],
                                               'menu_item': slashed_path[-1]})
