from rest_framework import serializers
from .models import ExcelPlanilha

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelPlanilha
        fields = '__all__'