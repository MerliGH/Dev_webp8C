from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pendientes, name='lista_pendientes'),
    path('crear/', views.crear_pendiente, name='crear_pendiente'),
    path('editar/<int:pk>/', views.editar_pendiente, name='editar_pendiente'),
    path('eliminar/<int:pk>/', views.eliminar_pendiente, name='eliminar_pendiente'),

    path('solo_ids/', views.lista_ids, name='solo_ids'),
    path('ids_titles/', views.lista_ids_titles, name='ids_titles'),
    path('sin_resolver/', views.lista_sin_resolver, name='sin_resolver'),
    path('resueltos/', views.lista_resueltos, name='resueltos'),
    path('ids_userid/', views.lista_ids_user, name='ids_userid'),
    path('resueltos_userid/', views.lista_resueltos_user, name='resueltos_userid'),
    path('sin_resolver_userid/', views.lista_sin_resolver_user, name='sin_resolver_userid'),

    path('json_pendientes/', views.lista_pendientes_desde_json, name='json_pendientes'),

]
