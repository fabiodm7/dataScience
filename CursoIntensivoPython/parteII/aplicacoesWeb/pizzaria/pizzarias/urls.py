from django.urls import path

from . import views

app_name = 'pizzarias'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('menu/<int:sabor_id>/',views.sabor,name='sabor'),
]