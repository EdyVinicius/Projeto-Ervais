from Comentario import Comentario

class Hotel:
    
    def __init__(self, nome, localizacao, tipo_acomodacao, preco, descricao, amenidades, disponibilidade, informacoes_contato):
        self.nome = nome
        self.localizacao = localizacao
        self.tipo_acomodacao = tipo_acomodacao
        self.preco = preco
        self.descricao = descricao
        self.amenidades = amenidades
        self.disponibilidade = disponibilidade
        self.informacoes_contato = informacoes_contato
        self.comentarios = []

    def adicionar_comentario(self, comentario: Comentario):
        self.comentarios.append(comentario)

    def remover_comentario(self, comentario: Comentario):
        self.comentarios.remove(comentario)
