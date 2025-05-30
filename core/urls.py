from django.urls import path
from core import views



app_name = 'core'
urlpatterns =[
    path('menu/content/', views.MenuView.as_view(), name='menu-content'),
    path('menu/content-specified/<str:category>/', views.menu_specified, name='menu-content-specified'),
    path('menu/content-specified/<str:category>/<int:item_id>/', views.specified_item, name='specified-item'),
    path('cart/', views.cart, name='cart'),
    path('after_payment', views.after_payment, name='after_payment'),
]