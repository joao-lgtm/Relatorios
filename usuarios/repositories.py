from .models import Usuario

class UsuarioRepository:
    @staticmethod
    def criar(dados):
        return Usuario.objects.create_user(**dados)

    @staticmethod
    def listar():
        return Usuario.objects.all()
