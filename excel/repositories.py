from .models import ExcelPlanilha

class ExcelRepository:
    @staticmethod
    def criar(dados):
        return ExcelPlanilha.objects.create(**dados)

    @staticmethod
    def existe_planilha(nome_planilha):
        return ExcelPlanilha.objects.filter(nome=nome_planilha).exists()