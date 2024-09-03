class HistoriaCidade:
    
    def __init__(self, descricao, imagens):
        self.descricao = descricao
        self.imagens = imagens

    def adicionar_imagem(self, imagem):
        self.imagens.append(imagem)

    def remover_imagem(self, imagem):
        self.imagens.remove(imagem)
