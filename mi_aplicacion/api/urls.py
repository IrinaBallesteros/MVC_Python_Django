from django.urls import path
from .views import UsuarioView, UsuarioDetailView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),  
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='detalle_usuario'), 
]
