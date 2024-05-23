# main.py
from Biblioteca import Biblioteca

from Libro import Libro

def main():
    biblioteca = Biblioteca("Biblioteca Central")
    while True:
        print("\nMenú:")
        print("1. Mostrar todos los libros disponibles")
        print("2. Prestar un libro")
        print("3. Recibir un libro")
        print("4. Agregar un libro")
        print("5. Guardar biblioteca en JSON")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.mostrar_libros_disponibles()
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a recibir: ")
            biblioteca.recibir_libro(titulo)
        elif opcion == "4":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año_publicacion = input("Ingrese el año de publicación del libro: ")
            disponible = True
            unidades = int(input("Ingrese la cantidad de unidades: "))
            libro = Libro(titulo, autor, año_publicacion, disponible, unidades)
            biblioteca.agregar_libro(libro)
        elif opcion == "5":
            biblioteca.guardar_en_json("biblioteca.json")
        elif opcion == "6":
            biblioteca.guardar_en_json("biblioteca.json")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
