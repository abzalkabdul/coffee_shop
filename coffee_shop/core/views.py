from django.views import generic
from django.shortcuts import render
from .models import Drinks, Food
from django.shortcuts import render

class MenuView(generic.ListView):
    template_name = "menu.html"

    def get_queryset(self):
        return list(Drinks.objects.all()) + list(Food.objects.all())


def rewards_view(request):
    return render(request, 'rewards.html')


def gift_cards_view(request):
    return render(request, 'gift_cards.html')
