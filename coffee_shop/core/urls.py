from django.urls import path
from core import views



app_name = 'core'
urlpatterns =[
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('rewards/', views.rewards_view, name='rewards'),
    path('gift_cards/', views.gift_cards_view, name='gift_cards'),

]