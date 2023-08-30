from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('adicionar/',views.adicionar, name='adicionar'),
    path('editar/<uuid:id_livro>',views.editar, name='editar'),
    path('excluir/<uuid:id_livro>',views.excluir, name='excluir'),
]