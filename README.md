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