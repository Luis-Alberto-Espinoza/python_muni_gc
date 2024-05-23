import json
from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

class TipoHabitacion:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

class Habitacion:
    def __init__(self, id, tipo_habitacion_id):
        self.id = id
        self.tipo_habitacion_id = tipo_habitacion_id

class Reserva:
    def __init__(self, id, fecha_reserva, fecha_entrada, fecha_salida, habitacion_id, usuario_id):
        self.id = id
        self.fecha_reserva = fecha_reserva
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.habitacion_id = habitacion_id
        self.usuario_id = usuario_id

    def se_superpone(self, fecha_entrada, fecha_salida):
        reserva_fecha_entrada = datetime.strptime(self.fecha_entrada, "%Y-%m-%d")
        reserva_fecha_salida = datetime.strptime(self.fecha_salida, "%Y-%m-%d")
        fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d")
        fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
        return (fecha_entrada < reserva_fecha_salida and fecha_salida > reserva_fecha_entrada)

class SistemaReservas:
    def __init__(self, data):
        self.data = data
        self.usuarios = {usuario["id"]: Usuario(**usuario) for usuario in data["usuarios"]}
        self.tipos_habitacion = {tipo["id"]: TipoHabitacion(**tipo) for tipo in data["tipos_habitacion"]}
        self.habitaciones = {habitacion["id"]: Habitacion(**habitacion) for habitacion in data["habitaciones"]}
        self.reservas = {reserva["id"]: Reserva(**reserva) for reserva in data["reservas"]}

    def guardar_en_json(self):
        with open('./baseDeDatos.json', 'w') as f:
            json.dump(self.data, f, indent=4)

    def habitaciones_disponibles(self, fecha_entrada, fecha_salida, tipo_habitacion_id):
        habitaciones_disponibles = []
        for habitacion in self.habitaciones.values():
            if habitacion.tipo_habitacion_id == tipo_habitacion_id:
                disponible = all(not reserva.se_superpone(fecha_entrada, fecha_salida) 
                                 for reserva in self.reservas.values() 
                                 if reserva.habitacion_id == habitacion.id)
                if disponible:
                    habitaciones_disponibles.append(habitacion.id)
        return habitaciones_disponibles

    def hacer_reserva(self, fecha_entrada, fecha_salida, tipo_habitacion_id, usuario_id):
        disponibles = self.habitaciones_disponibles(fecha_entrada, fecha_salida, tipo_habitacion_id)
        if disponibles:
            id_habitacion = disponibles[0]
            nueva_reserva = {
                "id": max(self.reservas.keys()) + 1 if self.reservas else 1,
                "fecha_reserva": datetime.now().strftime("%Y-%m-%d"),
                "fecha_entrada": fecha_entrada,
                "fecha_salida": fecha_salida,
                "habitacion_id": id_habitacion,
                "usuario_id": usuario_id
            }
            self.agregar_objeto(nueva_reserva, "reservas", "reservas")
            print(f"Reserva realizada con éxito: {nueva_reserva}")
            return nueva_reserva
        else:
            print("No hay habitaciones disponibles para las fechas y tipo seleccionados.")
            return None

    def eliminar_reserva(self, id_reserva):
        if id_reserva in self.reservas:
            del self.reservas[id_reserva]
            self.data["reservas"] = list(self.reservas.values())
            self.guardar_en_json()
            print(f"Reserva con ID {id_reserva} eliminada exitosamente.")
        else:
            print(f"No se encontró ninguna reserva con ID {id_reserva}.")

    def averiguar_id(self, nombre, apellido):
        for usuario in self.usuarios.values():
            if usuario.nombre == nombre and usuario.apellido == apellido:
                return usuario.id
        print(f"No se encontró ningún usuario con el nombre {nombre} {apellido}.")
        return None

    def agregar_objeto(self, nuevo_elemento, diccionario, nombre_objeto):
        lista_objetos = self.data.get(diccionario, [])
        nuevo_elemento["id"] = max(item["id"] for item in lista_objetos) + 1 if lista_objetos else 1
        lista_objetos.append(nuevo_elemento)
        self.data[nombre_objeto] = lista_objetos
        self.guardar_en_json()
        if diccionario == "usuarios":
            self.usuarios[nuevo_elemento["id"]] = Usuario(**nuevo_elemento)
        elif diccionario == "reservas":
            self.reservas[nuevo_elemento["id"]] = Reserva(**nuevo_elemento)

    def nuevo_usuario(self, nuevo_usuario):
        self.agregar_objeto(nuevo_usuario, "usuarios", "usuarios")
        print("Se agrego el nuevo usuario")
        id = self.averiguar_id(nuevo_usuario["nombre"], nuevo_usuario["apellido"])
        return id 

    def mostrar_reservas_por_tipo(self, tipo_habitacion_id):
        print(f"Reservas para el tipo de habitación con ID {tipo_habitacion_id}:")
        for reserva in self.reservas.values():
            habitacion_id = reserva.habitacion_id
            habitacion = self.habitaciones.get(habitacion_id)
            if habitacion and habitacion.tipo_habitacion_id == tipo_habitacion_id:
                print(f"ID de Reserva: {reserva.id}, Fecha de Entrada: {reserva.fecha_entrada}, Fecha de Salida: {reserva.fecha_salida}, ID de Habitación: {habitacion_id}")
        if not any(reserva.habitacion_id == tipo_habitacion_id for reserva in self.reservas.values()):
            print("No se encontraron reservas para este tipo de habitación.")

if __name__ == '__main__':
    with open('./reserva_Hotel_poo/baseDeDatos.json', 'r') as f:
        data = json.load(f)
    sistema = SistemaReservas(data)
