class Perfil:
    
    def __init__(self, nome, preferencias, informacoesPessoais):
        self.nome = nome
        self.preferencias = preferencias
        self.informacoesPessoais = informacoesPessoais

    def editar_informacoes(self, novasInformacoes):
        self.informacoesPessoais = novasInformacoes

    def editar_preferencias(self, novasPreferencias):
        self.preferencias = novasPreferencias
