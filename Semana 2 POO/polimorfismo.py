class Ave:
    def hablar(self):
        print("Algunas aves hacen sonidos.")

class Loro(Ave):
    def hablar(self):
        print("El loro dice: ¡Hola!")

class Canario(Ave):
    def hablar(self):
        print("El canario canta: ¡Pío pío!")

# Función polimórfica
def hacer_hablar(ave):
    ave.hablar()

# Crear objetos
mi_loro = Loro()
mi_canario = Canario()

# Usar polimorfismo
hacer_hablar(mi_loro)
hacer_hablar(mi_canario)
