from rest_framework import serializers
from .models import Consultas

# Serializer completo (para detalhes)
class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'

# Serializer resumido (somente id e nome)
class ConsultasIdNomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = ['id', 'nome']
