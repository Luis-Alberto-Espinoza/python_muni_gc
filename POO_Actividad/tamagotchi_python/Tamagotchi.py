class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 50
        self.humor = ""
        self.vivo = True

    def mostrar_estado(self):
        estado = "\n"
        estado += f"{self.nombre}:\n"
        estado += f"Nivel de energía: {self.energia}\n"
        estado += f"Nivel de hambre: {self.hambre}\n"
        estado += f"Nivel de felicidad: {self.felicidad}\n"
        self.actualizar_humor()
        estado += f"Estado de humor: {self.humor}\n"
        estado += "\n"
        print(estado)

    def alimentar(self):
        self.hambre -= 10
        if self.hambre < 0:
            self.hambre = 0
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
        self.verificar_estado()
        self.mostrar_estado()

    def jugar(self):
        self.felicidad += 20
        if self.felicidad > 100:
            self.felicidad = 100
        self.energia -= 18
        if self.energia < 0:
            self.energia = 0
        self.hambre += 10
        if self.hambre > 100:
            self.hambre = 100
        self.verificar_estado()
        self.mostrar_estado()

    def dormir(self):
        self.energia += 40
        if self.energia > 100:
            self.energia = 100
        self.hambre += 5
        if self.hambre > 100:
            self.hambre = 100
        self.verificar_estado()
        self.mostrar_estado()

    def actualizar_humor(self):
        if self.felicidad <= 20:
            self.humor = "enojado"
        elif 21 <= self.felicidad <= 40:
            self.humor = "triste"
        elif 41 <= self.felicidad <= 60:
            self.humor = "indiferente"
        elif 61 <= self.felicidad <= 80:
            self.humor = "feliz"
        else:
            self.humor = "euforico"

    def verificar_estado(self):
        if self.hambre >= 20:
            self.energia -= 20
            if self.energia < 0:
                self.energia = 0
            self.felicidad -= 30
            if self.felicidad < 0:
                self.felicidad = 0
        if self.energia == 0:
            print("Muerto")
            self.vivo = False
        else:
            self.hambre = max(0, min(self.hambre, 100))
            self.energia = max(0, min(self.energia, 100))
            self.felicidad = max(0, min(self.felicidad, 100))


nombre = input("Ingrese nombre de su Tamagotchi: ")
tamagotchi = Tamagotchi(nombre)

tamagotchi.mostrar_estado()

while tamagotchi.vivo:
    print("\n1. Alimentar\n2. Jugar\n3. Dormir\n4. Salir")

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        tamagotchi.alimentar()
    elif opcion == 2:
        tamagotchi.jugar()
    elif opcion == 3:
        tamagotchi.dormir()
    elif opcion == 4:
        break
    else:
        print("Opción inválida")
