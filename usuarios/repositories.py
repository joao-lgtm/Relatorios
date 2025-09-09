from .models import Usuario

class UsuarioRepository:
    @staticmethod
    def criar(dados):
        return Usuario.objects.create_user(**dados)

    @staticmethod
    def list():
        return Usuario.objects.all()
