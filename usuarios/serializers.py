from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario.objects.create_user(
            email=validated_data['email'],
            nome=validated_data['nome'],
            password=password
        )
        return usuario
