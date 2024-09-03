class MenuNavegacao:
    
    def __init__(self, itens):
        self.itens = itens

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        self.itens.remove(item)
