import json
from Libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.cargar_desde_json("biblioteca.json")
  

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro.libros_prestados < libro.unidades:
                print(libro)

    def prestar_libro1(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f'El libro "{titulo}" ha sido prestado.')
                return
        print(f'El libro "{titulo}" no está disponible.')


    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.libros_prestados < libro.unidades:
                    libro.libros_prestados += 1
                    if libro.libros_prestados == libro.unidades:
                        libro.disponible = False
                    self.guardar_en_json("biblioteca.json")  # Guardar cambios en el archivo JSON
                    print(f'El libro "{titulo}" ha sido prestado.')
                    return
                else:
                    print(f'No hay ejemplares disponibles del libro "{titulo}".')
                    return
        print(f'El libro "{titulo}" no está registrado en la biblioteca.')

    def recibir_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.libros_prestados > 0:
                    libro.libros_prestados -= 1
                    libro.disponible = True
                    self.guardar_en_json("biblioteca.json")  # Guardar cambios en el archivo JSON
                    print(f'El libro "{titulo}" ha sido devuelto.')
                    return
                else:
                    print(f'El libro "{titulo}" no estaba prestado.')
                    return
        print(f'El libro "{titulo}" no está registrado en la biblioteca.')

    def guardar_en_json(self, archivo):
        libros_dict = [libro.__dict__ for libro in self.libros]
        archivo_path = "./POO_Actividad/biblioteca_python/" + archivo
        with open(archivo_path, 'w') as f:
            json.dump(libros_dict, f, indent=4)
        print(f"Biblioteca guardada en {archivo_path}.")

    def cargar_desde_json(self, archivo):
        archivo_path = "./POO_Actividad/biblioteca_python/" + archivo
        with open(archivo_path, 'r') as archivo:
            datos = json.load(archivo)
            for dato in datos:
                libro = Libro(dato['titulo'], dato['autor'], dato['año_publicacion'], dato['disponible'], dato.get('unidades', 1), dato.get('libros_prestados', 0))
                self.libros.append(libro)