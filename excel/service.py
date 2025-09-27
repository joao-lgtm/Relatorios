from os import mkdir

from django.http import FileResponse

from excel.repositories import ExcelRepository
import os
from django.conf import settings
from utils.BaseResponse import BaseResponse
import pandas as pd
import numpy as np


class ExcelService:
    @staticmethod
    def criar(file, usuario, nome, permission):
        if not file:
            return BaseResponse.error(
                message="Nenhum arquivo enviado",
                errors=None,
                status_code=400
            )

        if ExcelRepository.existe_planilha(nome):
            return BaseResponse.error(
                message="Já existe um arquivo com esse nome",
                errors=None,
                status_code=400
            )

        save_dir = settings.EXCEL_UPLOAD_DIR
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(settings.EXCEL_UPLOAD_DIR, file.name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        dados = {
            'nome': nome,
            'usuario': usuario,
            'permission': permission
        }

        planilha = ExcelRepository.criar(dados)

        return BaseResponse.success(
            message="Arquivo salvo com sucesso",
            data={"id": planilha.id, "nome": planilha.nome},
            status_code=201
        )

    @staticmethod
    def pega_planilha_excel(nome):
        if not ExcelRepository.existe_planilha(nome):
            return BaseResponse.error(
                message="Não existe um arquivo salvo com esse nome",
                errors=None,
                status_code=400
            )

        caminho = os.path.join(settings.EXCEL_UPLOAD_DIR, nome)

        if not os.path.exists(caminho):
            return BaseResponse.error(
                message=f"Arquivo não encontrado no servidor: {caminho}",
                errors=None,
                status_code=404
            )

        return FileResponse(open(caminho, "rb"), as_attachment=True, filename=nome)

    @staticmethod
    def pega_planilha_json(nome):
        if not ExcelRepository.existe_planilha(nome):
            return BaseResponse.error(
                message="Não existe um arquivo salvo com esse nome",
                errors=None,
                status_code=400
            )

        caminho = os.path.join(settings.EXCEL_UPLOAD_DIR, nome)

        if not os.path.exists(caminho):
            return BaseResponse.error(
                message=f"Arquivo não encontrado no servidor: {caminho}",
                errors=None,
                status_code=404
            )

        df = pd.read_excel(caminho)
        df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
        data = df.to_dict(orient="records")

        return BaseResponse.success(
            message="Planilha carregada",
            data=data,
            status_code=200
        )


