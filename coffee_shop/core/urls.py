from django.urls import path
from core import views



app_name = 'core'
urlpatterns =[
    path('menu/', views.MenuView.as_view(), name='menu')
]