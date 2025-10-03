from django.urls import path
from .views import ConsultasVwView, ListaConsultasVwView

urlpatterns = [
    path('consultar-relatorios/', ConsultasVwView.as_view(), name='consult-relatorios'),
    path('listar-relatorios/', ListaConsultasVwView.as_view(), name='listar-relatorios'),
]
