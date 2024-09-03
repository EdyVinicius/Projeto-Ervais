from Evento import Evento

class CalendarioEventos:
    
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento: Evento):
        self.eventos.append(evento)

    def remover_evento(self, evento: Evento):
        self.eventos.remove(evento)
