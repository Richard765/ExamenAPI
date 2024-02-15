from django.contrib import admin
from django.urls import path
from socios import views

urlpatterns = [
    path('socios/crear/', views.crear_socio),
    path('socios/<int:pk>/modificar/', views.modificar_contraseña),
    path('socios/lista/', views.lista_socios),
]
