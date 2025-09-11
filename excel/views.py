import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from excel.service import ExcelService

class ExcelUploadSaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")
        usuario = request.user
        permission = request.data.get("permission", 0)

        if not file:
            return Response({"error": "Nenhum arquivo enviado"}, status=status.HTTP_400_BAD_REQUEST)

        ExcelService.criar(
            file=file,
            usuario=usuario,
            nome=file.name,
            permission=permission
        )

        return Response({"message": f"Arquivo salvo: {file.name}"}, status=status.HTTP_201_CREATED)
