class Comentario:

    def __init__(self, autor, texto, data):
        self.autor = autor
        self.texto = texto
        self.data = data

    def visualizar_comentario(self):
        return (f"Autor: {self.autor} | Data: {self.data}\n Comentario: {self.texto}")
