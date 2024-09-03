from Perfil import Perfil

class Usuario:
    
    def __init__(self, nome, email, senha, perfil: Perfil):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil

    def cadastrar(self):
        pass # Cadastrar o usuário

    def autenticar(self):
        pass # Autenticar o usuário

    def recuperar_senha(self):
        pass # Recuperar a senha do usuário

    def visualizar_perfil(self):
        pass # Visualizar o perfil do usuário

    def editar_perfil(self, novo_perfil: Perfil):
        self.perfil = novo_perfil
