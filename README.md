# POO en Python

- El paradigma de POO està basado en una abstracciòn del mundo real que nos va a permitir desarrollar programas de forma màs cercana a como vemos el mundo, pensando en objetos que tenemos adelante y acciones que podemos hacer con ellos. 

## Clase 

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancias.
- La clase es la definiciòn del concepto del mundo real y los objetos o instancias son el propio objeto del mundo real.
- Las clases estàn compuestas por dos elementos: atributos y mètodos.

### Atributos
- Informaciòn que almacena la clase

### Mètodos 
- Las operaciones que pueden realizar las clases

## Definiciòn de una clase en Python 

```Python
class NombreClase:

    def __init__(self, variable1, variable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2

    def nombreMetodo(self):
        bloqueCodigo
```
### Componentes

```class```: palabra reservada en Python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en Python que se utiliza para definir tanto el constructor de la clase (mètodo que se ejecuta la primera vez que usas una clase) como los diferentes mètodos que tiene.

```__init__```: palabra reservada en Python para definir el mètodo constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto de una clase.

```(self, variableX)```: paràmetro del constructor de la clase. El paràmetro self es obligatorio y despuès puedes tener tantos paràmetros como quieras. La forma de añadir paràmetros es la misma que en las funciones.

```self.AtributoX```: forma de utilizaciòn y acceso a los atributos de la clase. 

```nombreMetodo```: nombre del mètodo de la clase. 

```self```: paràmetros del mètodo. El paràmetro self es obligatorio y despuès puedes tener tantos paràmetros como quieras. La forma de añadir paràmetros es la misma que en las funciones.

```bloqueCodigo```: instrucciones que ejecutarà el mètodo.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
    - Puedes definir tantos atributos como necesites.
    - Puedes definir tantos mètodos como necesites.
    - Puedes definir tantos paràmetros en el constructor y en los mètodos como necesites. 

## Composiciòn
- Consiste en la creaciòn de nuevas clases a partir de otras clases ya existentes que actùan como elementos compositores de la nueva.
- Las clases existentes seràn atributos de la nueva clase.
- En POO la composiciòn significa que entre las dos clases existe una relaciòn del tipo "tiene un".
- Ejemplo: 
    - Una coordenada en dos dimensiones està compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, èsto podrìa ser una clase. Un cuadrado està compuesto por cuatro coordenadas que son los cuatro vertices, èsto podrìa ser una clase que està compuesta por cuatro clases del objeto coordenada.

## Encapsulación
- Se trata de la protección de los datos de usos o accesos no controlados.
- Los datos (atributos) que componen una clase pueden ser de dos tipos:
    - Públicos:  los datos son accesibles sin control, es decir, los datos pueden ser usados sin ningún tipo de mecanismo que proteja ante usos no autorizados o indebidos.
    - Privados: los datos no pueden ser accedidos sin control y para acceder a ellos se deberá implementar un método que acceda a ellos.  De esta forma, los datos serán accedidos única y directamente por la propia clase.
- La encapsulación no solo puede realizarse sobre los atributos de la clase, también es posible realizarla sobre los métodos, es decir, aquellos métodos que indiquemos que son privados no podrán ser utilizados por elementos externos al propio objeto.
- La definición de atributos y mètodos privados se realiza incluyendo los caracteres "__" (dos guiones de piso) entre la palabra "self" y el nombre del atributo.

## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono

## Actividad:
- Consulte un ejemplo práctico del uso de herencia múltiple en Python

### Bibliografía
Moreno, A. y Córcoles, S.  (2020).  Python práctica.  Herramientas, conceptos y técnicas.  Ediciones de la U.