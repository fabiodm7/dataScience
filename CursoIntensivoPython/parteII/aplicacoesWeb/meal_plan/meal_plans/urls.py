"""Define padrões de URL para Mean Plan"""
from django.urls import path

from . import views

app_name = 'mean_plans'

urlpatterns = [
    # Página inicial
    path('',views.index,name='index')
]