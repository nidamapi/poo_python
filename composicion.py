# Composiciòn

"""Una coordenada en dos dimensiones està compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, èsto podrìa ser una clase. Un cuadrado està compuesto por cuatro coordenadas que son los cuatro vertices, èsto podrìa ser una clase que està compuesta por cuatro clases del objeto coordenada"""

# clase Coordenada

class Coordenada:
    #mètodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # mètodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.X, ",", self.Y, ")")

# clase Cuadrado

class Cuadrado:

    # mètodo constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # mètodo para mostrar los vèrtices
    def mostrarVertices(self):
        print("El cuadrado està compuesto por los siguientes vèrtices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

# mètodo principal
def main():
    # input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()
    
    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

if __name__== "__main__":
    main()
