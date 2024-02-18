import os
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from .utils import info

User = get_user_model()

DJANGO_SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME', default='super')
DJANGO_SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL', default='veryPriv@ate.com')
DJANGO_SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD', default='super')


class Command(BaseCommand):
    _class = User
    name = 'SUPERUSER'

    @info
    def handle(self, *args, **kwargs):
        self._class.objects.create_superuser(
            DJANGO_SUPERUSER_USERNAME,
            DJANGO_SUPERUSER_EMAIL,
            DJANGO_SUPERUSER_PASSWORD)
