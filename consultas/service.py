from rest_framework.views import APIView

from consultas.repositories import ConsultaRepository
from consultas.serializer import ConsultasSerializer
from utils.BaseResponse import BaseResponse
from utils.connection import sql
import pandas as pd

class ConsultasService:

    @staticmethod
    def consulta(nome):
        if not ConsultaRepository.existe_consultas(nome):
            return BaseResponse.error(
                message="Não existe uma consulta com esse nome",
                errors=None,
                status_code=400
            )

        consulta = ConsultaRepository.consulta(nome)
        serializer = ConsultasSerializer(consulta)

        vw = sql(serializer.data.get("consultas"))

        print(vw)

        return BaseResponse.success(
            message="Cons",
            data=vw,
            status_code=200
        )






