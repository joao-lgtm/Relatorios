from excel.repositories import ExcelRepository
import os
from django.conf import settings

class ExcelService:
    @staticmethod
    def criar(file, usuario, nome, permission):
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

        return ExcelRepository.criar(dados)
