"""Define os padrões de URL para Blogs"""

from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    # Página inicial
    path('',views.index,name='index'),
    # path('',views.blogposts,name='index'),

    # Mostra todas as postagens
    path('blogposts',views.blogposts,name='blogposts'),

    # Escreve um novo post
    path('new_post',views.new_post,name='new_post'),

    # Edita um post
    path('edit_post/<int:blogpost_id>',views.edit_post,name='edit_post'),
]