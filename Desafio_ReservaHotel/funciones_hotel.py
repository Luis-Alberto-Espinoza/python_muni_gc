import json
from datetime import datetime

with open('./baseDeDatos.json', 'r') as f:
    data = json.load(f)

def guardar_en_json(data):
    with open('./baseDeDatos.json', 'w') as f:
        json.dump(data, f, indent=4)  


usuarios = {usuario["id"]: usuario for usuario in data["usuarios"]}
tipos_habitacion = {tipo["id"]: tipo for tipo in data["tipos_habitacion"]}
habitaciones = {habitacion["id"]: habitacion for habitacion in data["habitaciones"]}
reservas = {reserva["id"]: reserva for reserva in data["reservas"]}

def reserva_se_superpone(reserva, fecha_entrada, fecha_salida):
    reserva_fecha_entrada = datetime.strptime(reserva["fecha_entrada"], "%Y-%m-%d")
    reserva_fecha_salida = datetime.strptime(reserva["fecha_salida"], "%Y-%m-%d")
    fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d")
    fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
    if (fecha_entrada < reserva_fecha_salida and fecha_salida > reserva_fecha_entrada):
        return True
    return False

def habitaciones_disponibles(reservas, fecha_entrada, fecha_salida, tipo_habitacion_id, habitaciones):
    habitaciones_disponibles = []
    for habitacion in habitaciones.values():
        habitacion_id = habitacion["id"]
        disponible = True
        for reserva in reservas.values():
            if reserva["habitacion_id"] == habitacion_id:
                if reserva_se_superpone(reserva, fecha_entrada, fecha_salida):
                    disponible = False
                    break
        if disponible and habitacion["tipo_habitacion_id"] == tipo_habitacion_id:
            habitaciones_disponibles.append(habitacion_id)
    return habitaciones_disponibles

def hacer_reserva(fecha_entrada, fecha_salida, tipo_habitacion_id, usuario_id):
    disponibles = disponibilidad(fecha_entrada, tipo_habitacion_id, fecha_salida)
    if disponibles:
        id_habitacion = disponibles[0]
        nueva_reserva = {
            "fecha_reserva": datetime.now().strftime("%Y-%m-%d"),  # Fecha de la reserva (hoy)
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida,
            "habitacion_id": id_habitacion,
            "usuario_id": usuario_id
        }
        agregar_objeto(nueva_reserva, "reservas", "reservas")
        print(f"Reserva realizada con éxito: {nueva_reserva}")
        return nueva_reserva
    else:
        print("No hay habitaciones disponibles para las fechas y tipo seleccionados.")
        return None
    
def eliminar_reserva(id_reserva):
    if id_reserva in reservas:
        del reservas[id_reserva]
        data["reservas"] = list(reservas.values())  
        guardar_en_json(data)  
        print(f"Reserva con ID {id_reserva} eliminada exitosamente.")
    else:
        print(f"No se encontró ninguna reserva con ID {id_reserva}.")
def averiguar_id(nombre, apellido):
    for usuario in usuarios.values():
        if usuario["nombre"] == nombre and usuario["apellido"] == apellido:
            return usuario["id"]
    print(f"No se encontró ningún usuario con el nombre {nombre} {apellido}.")
    return None

def agregar_objeto(nuevo_elemento,diccionario, nombre_objeto):
    lista_objetos = data.get(diccionario, [])
    if lista_objetos:
        ultimo_id = max(item["id"] for item in lista_objetos)
        nuevo_elemento["id"] = ultimo_id + 1
    else:
        nuevo_elemento["id"] = 1
    lista_objetos.append(nuevo_elemento)
    data[nombre_objeto] = lista_objetos
    guardar_en_json(data)
    if diccionario == "usuarios":
        global usuarios
        usuarios[nuevo_elemento["id"]] = nuevo_elemento
    elif diccionario == "reservas":
        global reservas
        reservas[nuevo_elemento["id"]] = nuevo_elemento    

def disponibilidad(fecha_entrada, tipo_habitacion_id, fecha_salida):
    disponibles = habitaciones_disponibles(reservas, fecha_entrada, fecha_salida, tipo_habitacion_id, habitaciones)
    tipo_habitacion = tipos_habitacion[tipo_habitacion_id]["tipo"]
    print(f"Habitaciones disponibles para reservar entre {fecha_entrada} y {fecha_salida} del tipo {tipo_habitacion}: {disponibles}")
    return disponibles

def nuevo_usuario(nuevo_usuario):
    agregar_objeto(nuevo_usuario, "usuarios", "usuarios")
    print("Se agrego el nuevo usuario")
    id = averiguar_id(nuevo_usuario["nombre"], nuevo_usuario["apellido"])
    return id 

def mostrar_reservas_por_tipo(tipo_habitacion_id):
    print(f"Reservas para el tipo de habitación con ID {tipo_habitacion_id}:")
    for reserva in reservas.values():
        habitacion_id = reserva["habitacion_id"]
        habitacion = habitaciones.get(habitacion_id)
        if habitacion and habitacion["tipo_habitacion_id"] == tipo_habitacion_id:
            print(f"ID de Reserva: {reserva['id']}, Fecha de Entrada: {reserva['fecha_entrada']}, Fecha de Salida: {reserva['fecha_salida']}, ID de Habitación: {habitacion_id}")
    if not any(reserva["habitacion_id"] == tipo_habitacion_id for reserva in reservas.values()):
        print("No se encontraron reservas para este tipo de habitación.")

if __name__ == '__main__':
    pass
