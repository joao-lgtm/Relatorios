from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .service import UsuarioService

class UsuarioCreateView(APIView):
    def post(self, request):
        return UsuarioService.criar(request.data)

class UsuarioListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return UsuarioService.listar()
