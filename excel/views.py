from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from excel.service import ExcelService
from usuarios.service import UsuarioService
from utils.BaseResponse import BaseResponse


class ExcelUploadSaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")
        usuario = request.user
        permission = request.data.get("permission", 0)

        return ExcelService.criar(file, usuario, file.name, permission)


class ExcelDownloadView(APIView):
    def get(self, request):
        nome = request.GET.get("nome")
        if not nome:
            return ExcelService.pega_planilha_excel("")
        return ExcelService.pega_planilha_excel(nome)

class ExcelJsonView(APIView):
    def get(self, request = None):
        nome = request.GET.get("nome")
        if not nome:
            return ExcelService.pega_planilha_json("")
        return ExcelService.pega_planilha_json(nome)
