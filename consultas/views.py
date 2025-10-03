from rest_framework.views import APIView

from consultas.service import ConsultasService


# Create your views here.
class ConsultasVwView(APIView):
    def get(self, request):
        nome = request.GET.get("nome")
        return ConsultasService.consulta(nome)

class ListaConsultasVwView(APIView):
    def get(self, request):
        return ConsultasService.pegaTodasConsultas()

