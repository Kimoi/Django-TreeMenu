from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.URLField(blank=True)  # default length of 200
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
