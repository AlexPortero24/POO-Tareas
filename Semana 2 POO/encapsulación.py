class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    def get_edad(self):
        return self.__edad

# Crear objeto
persona = Persona("Ana", 25)

# Mostrar datos
persona.mostrar_datos()

# Cambiar edad de forma segura
persona.set_edad(30)
print(f"Nueva edad: {persona.get_edad()}")

# Intentar asignar una edad inválida
persona.set_edad(-5)
