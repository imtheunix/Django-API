from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notas/', views.getNotas),
    path('notas/criar/', views.createNota),
    path('notas/<str:pk>/modificar/', views.updateNota),
    path('notas/<str:pk>/deletar/', views.deletarNota),
    path('notas/<str:pk>/', views.getNota),


]
