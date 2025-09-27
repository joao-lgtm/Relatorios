from django.urls import path
from .views import ConsultasVwView

urlpatterns = [
    path('consultarView/', ConsultasVwView.as_view(), name='consult-view'),
]
