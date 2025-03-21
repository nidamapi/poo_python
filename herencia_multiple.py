# Herencia mùltiple
"""La herencia múltiple en Python permite que una clase herede atributos y métodos de más de una clase base. Esto puede ser útil cuando deseas combinar comportamientos o propiedades de diferentes clases en una sola."""
"""Herencia: Una clase base.    Herencia múltiple: Varias clases base."""

# Ejemplo
"""Supongamos que tenemos dos clases base: Vehículo y Electrónico. Queremos crear una clase CocheEléctrico que herede tanto las propiedades de un vehículo como las de un dispositivo electrónico."""
# Clase base 1: Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print("Marca: " + self.marca + ", Modelo: " + self.modelo)

# Clase base 2: Electrónico
class Electronico:
    def __init__(self, bateria):
        self.bateria = bateria

    def cargar(self):
        print("Cargando batería de " + str(self.bateria) + "%.")

# Clase derivada: CocheElectrico
class CocheElectrico(Vehiculo, Electronico):
    def __init__(self, marca, modelo, bateria):
        # Inicializando las clases base
        Vehiculo.__init__(self, marca, modelo)
        Electronico.__init__(self, bateria)

    def conducir(self):
        print("Conduciendo el coche eléctrico.")

# Crear un objeto de la clase CocheElectrico
coche = CocheElectrico("Tesla", "Model S", 100)

# Usando métodos de las clases base
coche.mostrar_info()  # Método de Vehiculo
coche.cargar()        # Método de Electronico
coche.conducir()      # Método de CocheElectrico



