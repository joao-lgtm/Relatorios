from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from excel.service import ExcelService
from utils.BaseResponse import BaseResponse


class ExcelUploadSaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")
        usuario = request.user
        permission = request.data.get("permission", 0)

        return ExcelService.criar(file, usuario, file.name, permission)
