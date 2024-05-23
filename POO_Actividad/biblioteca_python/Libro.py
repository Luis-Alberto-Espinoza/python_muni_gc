class Libro():
    def __init__(self, titulo, autor, año_publicacion, disponible, unidades, libros_prestados=0):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = disponible
        self.unidades = unidades
        self.libros_prestados = libros_prestados

  
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Disponible: {self.disponible}, Unidades: {self.unidades}"
