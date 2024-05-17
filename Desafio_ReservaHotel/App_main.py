import funciones_hotel
def mostrar_menu():
    print("\nBienvenido al sistema de gestión de reservas:")
    print("1. Ver disponibilidad de habitaciones")
    print("2. Hacer una reserva")
    print("3. Eliminar una reserva")
    print("4. Mostrar reservas por tipo de habitación")
    print("5. Ingresar un nuevo Cliente")
    print("6. Salir\n")

def ejecutar_opcion(opcion):
    if opcion == 1:
        fecha_entrada = input("\nIngrese la fecha de entrada (YYYY-MM-DD): ")
        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
        tipo_habitacion_id = int(input("Ingrese el ID del tipo de habitación: "))
        funciones_hotel.disponibilidad(fecha_entrada, tipo_habitacion_id, fecha_salida)
    elif opcion == 2:
        fecha_entrada = input("\nIngrese la fecha de entrada (YYYY-MM-DD): ")
        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
        print("Ingrese el ID del tipo de habitación: ")
        print("Ingrese 1 par el tipo 'INDIVIDUAL' ")
        print("Ingrese 2 par el tipo 'DOBLE' ")
        tipo_habitacion_id = int(input("Ingrese 3 par el tipo 'SUITE' : "))
        usuario_id = int(input("Ingrese su ID de usuario: "))
        funciones_hotel.hacer_reserva(fecha_entrada, fecha_salida, tipo_habitacion_id, usuario_id)
    elif opcion == 3:
        id_reserva = int(input("\nIngrese el ID de la reserva que desea eliminar: "))
        funciones_hotel.eliminar_reserva(id_reserva)
    elif opcion == 4:
        print("\nIngrese el ID del tipo de habitación: ")
        tipo_habitacion_id = int(input("Para 'INDIVIDUAL' oprima el >> 1\nPara 'DOBLE' oprima el >> 2\nPara 'SUITE' oprima el >> 3 "))
        funciones_hotel.mostrar_reservas_por_tipo(tipo_habitacion_id)
    elif opcion == 5:
        nombre = input("\nIngrese el nombre del nuevo cliente: ")
        apellido = input("Ingrese el apellido del nuevo cliente: ")
        nuevo_usuario = {"nombre": nombre, "apellido": apellido}
        id= funciones_hotel.nuevo_usuario(nuevo_usuario)
        print ("el nuevo usuario tiene el id numero ", id)
    elif opcion == 6:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    ejecutar_opcion(opcion)
