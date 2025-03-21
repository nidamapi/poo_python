# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__Antigüedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
    
    def getAntigüedad(self):
        return self.__Antigüedad
    
    def setAntigüedad(self, antigüedad):
        self.__Antigüedad = antigüedad
    
    def getTutorias(self):
        return self.__Tutorias
    
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias
    
    def getTelefono(self):
        return self.__Telefono
    
    def setTelefono(self, telefono):
        self.__Telefono = telefono
    
    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tAntigüedad: ", self.__Antigüedad)
        print("\tTutorias: ", self.__Tutorias)
        print("\tTelefono: ", self.__Telefono)


# mètodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Néstor")
    alumno.setApellidos("Páez Sarmiento")
    alumno.setEdad(25)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    profesor = Profesor()
    profesor.setNombre("Nicolle")
    profesor.setApellidos("Macìas Piracòn")
    profesor.setEdad(50)
    profesor.setAntigüedad("30 años")
    profesor.setTutorias(["Lunes: 4:45pm a 10:00pm", "Martes: 2:00pm a 7:00pm", "Jueves 6:45am a 12:00pm"])
    profesor.setTelefono("3345001207")
    profesor.mostrarProfesor()
    

if __name__ == "__main__":
    main()

