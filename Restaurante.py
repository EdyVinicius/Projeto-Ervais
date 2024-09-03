from Comentario import Comentario
from Menu import Menu

class Restaurante:
    
    def __init__(self, nome, descricao, menu: Menu, horarioFuncionamento, informacoesContato):
        self.nome = nome
        self.descricao = descricao
        self.menu = menu
        self.horarioFuncionamento = horarioFuncionamento
        self.informacoesContato = informacoesContato
        self.comentarios = []

    def adicionar_comentario(self, comentario: Comentario):
        self.comentarios.append(comentario)

    def remover_comentario(self, comentario: Comentario):
        self.comentarios.remove(comentario)
