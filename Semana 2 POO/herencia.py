# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Clase hija que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")

# Crear objeto Auto
mi_auto = Auto("Toyota", "Corolla", 4)
mi_auto.mostrar_info()
