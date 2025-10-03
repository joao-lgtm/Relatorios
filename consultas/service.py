from rest_framework.views import APIView

from consultas.repositories import ConsultaRepository
from consultas.serializer import ConsultasSerializer, ConsultasIdNomeSerializer
from utils.BaseResponse import BaseResponse
from utils.connection import sql
import pandas as pd

from utils.traduzTipoColuna import traduzTipoColunas


class ConsultasService:
    @staticmethod
    def pegaTodasConsultas():
        relatorios = ConsultaRepository.todasConsultas()

        nomeRelatorios = ConsultasIdNomeSerializer(relatorios, many=True)
        return BaseResponse.success(
            message='Lista de consultas',
            data=nomeRelatorios.data,
            status_code=200
        )

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

        tc = traduzTipoColunas(vw)

        return BaseResponse.success(
            message="consulta encontrada com sucesso",
            data=tc,
            status_code=200
        )






