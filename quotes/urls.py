from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agregar_stock/', views.agregar_stock, name='agregar_stock'),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('eliminar-stock/', views.eliminar_stock, name='eliminar_stock'),
]
