from MenuNavegacao import MenuNavegacao
from Busca import Busca
from CalendarioEventos import CalendarioEventos

class PaginaPrincipal:
    def __init__(self, menuNavegacao: MenuNavegacao, destaquePromocoes, busca: Busca, calendarioEventos: CalendarioEventos):
        self.menuNavegacao = menuNavegacao
        self.destaquePromocoes = destaquePromocoes
        self.busca = busca
        self.calendarioEventos = calendarioEventos

    def mostrar_destaques(self):
        pass # Mostrar os destaques

    def realizar_busca(self, termos):
        return self.busca.realizar_busca(termos)

    def exibir_eventos(self):
        pass # Exibir os eventos
