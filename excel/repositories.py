from .models import ExcelPlanilha

class ExcelRepository:
    @staticmethod
    def criar(dados):
        return ExcelPlanilha.objects.create(**dados)