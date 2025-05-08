from django.views import generic
from django.shortcuts import render
from .models import Drinks, Food

class MenuView(generic.ListView):
    template_name = "menu.html"

    def get_queryset(self):
        return list(Drinks.objects.all()) + list(Food.objects.all())


