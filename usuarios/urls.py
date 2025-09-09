from django.urls import path
from .views import UsuarioCreateView, UsuarioListView

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuario-list'),
    path('cadastrar/', UsuarioCreateView.as_view(), name='usuario-create'),
]
