from .models import Usuario
from .repositories import UsuarioRepository
from .serializers import UsuarioSerializer
from utils.BaseResponse import BaseResponse
from rest_framework import status

class UsuarioService:
    @staticmethod
    def criar(data):
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            usuario = serializer.save()

            return BaseResponse.success(
                message="Usuário criado com sucesso",
                data=UsuarioSerializer(usuario).data,
                status_code=status.HTTP_201_CREATED
            )
        return BaseResponse.error(
            message="Erro ao criar usuário",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def listar():
        usuarios = UsuarioRepository.listar()
        serializer = UsuarioSerializer(usuarios, many=True)
        return BaseResponse.success(
            message="Lista de usuários recuperada com sucesso",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )
