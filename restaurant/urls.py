from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
]