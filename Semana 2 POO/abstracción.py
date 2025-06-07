from abc import ABC, abstractmethod

# Creamos una clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        # Método abstracto: debe ser implementado por las subclases
        pass

# Clase que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro dice: ¡Guau!")

# Clase que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato dice: ¡Miau!")

# Creamos instancias
perro = Perro()
gato = Gato()

# Usamos los métodos abstractos implementados
perro.hacer_sonido()
gato.hacer_sonido()
