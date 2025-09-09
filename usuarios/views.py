from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer
from .service import UsuarioService

class UsuarioCreateView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = UsuarioService.criar(serializer.validated_data)
            return Response('Usuario Criado com sucesso', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class UsuarioListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        usuarios = UsuarioService().listar()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


