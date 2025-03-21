# Encapsulaciòn

"""Una coordenada en dos dimensiones està compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, èsto podrìa ser una clase. Un cuadrado està compuesto por cuatro coordenadas que son los cuatro vertices, èsto podrìa ser una clase que està compuesta por cuatro clases del objeto coordenada"""

# clase Coordenada

class Coordenada:

    #mètodo constructor
    def __init__(self, x, y):
        # atributos privados
        self.__X = x
        self.__Y = y

    
    # mètodos de la lectura y escritura de cada atributo
    def get__X(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x

    def setY(self, y):
        self.__Y = y

    # mètodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")")

# clase Cuadrado

class Cuadrado:

    # mètodo constructor
    def __init__(self, v1, v2, v3, v4):
        # atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4
    
    # mètodos privados para mostrar los vèrtices
    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getx(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV1(self):
        print("(", self.__V2.getx(), ",", self.__V2.getY(), ")")

    def __mostrarCoordenadaV1(self):
        print("(", self.__V3.getx(), ",", self.__V3.getY(), ")")    

    def __mostrarCoordenadaV1(self):
        print("(", self.__V4.getx(), ",", self.__V4.getY(), ")")

    # mètodo para mostrar los vèrtices
    def mostrarVertices(self):
        print("El cuadrado està compuesto por los siguientes vèertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

# mètodo principal del mòdulo
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

    # Què ocurre si el mètodo getX() lo hacemos privado: __getX()?
    coordenada = Coordenada(3,4)
    print("(", coordenada.__getX(), ",", coordenada.getY(), ")")


if __name__ == "__main__":
    main()