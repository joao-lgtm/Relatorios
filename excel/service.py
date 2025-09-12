from excel.repositories import ExcelRepository
import os
from django.conf import settings
from utils.BaseResponse import BaseResponse


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
