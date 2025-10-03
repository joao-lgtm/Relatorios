from consultas.models import Consultas


class ConsultaRepository:
    @staticmethod
    def todasConsultas():
        return Consultas.objects.only('id', 'nome')

    @staticmethod
    def consulta(nome):
        return Consultas.objects.get(nome=nome)

    @staticmethod
    def existe_consultas(nome):
        return Consultas.objects.filter(nome=nome).exists()
