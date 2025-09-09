import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExcelUploadView(APIView):
    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "Nenhum arquivo enviado"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_excel(file)

            # Corrige NaN, NaT, Inf e -Inf → None
            df = df.replace({np.nan: None, np.inf: None, -np.inf: None})

            data = df.to_dict(orient="records")
            return Response({"rows": data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
