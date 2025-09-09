from .repositories import UsuarioRepository
from .models import Usuario
import requests

class UsuarioService:
    @staticmethod
    def criar(dados):
        return UsuarioRepository.criar(dados)

    @staticmethod
    def listar():
        usuarios = UsuarioRepository.list()

        return usuarios