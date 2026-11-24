# D=================================================================================================================== #
# Título: Ejercicio 2.	
# Crear una clase Estudiante que represente a un estudiante de primer año. 
# Sus atributos son: nombre, apellido, nota programación, nota álgebra, nota cálculo, y nota física. 
# Crear un método init que reciba valores para cada uno de los atributos. 
# Crear propiedades y setters que comprueben que los valores de los atributos son correctos. 
# Escribir un programa que cree un objeto de este tipo, solicite al usuario los valores de los campos por teclado e 
# imprima por pantalla la información del estudiante. 
# Autor: Miguel Jun Patricio Ferrer 
# Fecha: 24 / 11 / 26
# Version: 1.0
# D=================================================================================================================== #
class Estudiante:

    # Declaración de atributos
    def __init__(self, nombre: str, apellido: str, nota_programacion: float, nota_algebra: float, nota_calculo: float, nota_fisica: float):
        self.nombre = nombre
        self.apellido = apellido
        self.nota_programacion = nota_programacion
        self.nota_algebra = nota_algebra
        self.nota_calculo = nota_calculo
        self.nota_fisica = nota_fisica

    # Propiedades y setter
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, otro):
        if not isinstance(otro, str):
            raise TypeError("El nombre introducido es del tipo incorrecto")
        elif len(otro) < 0:
            raise ValueError("El nombre introducido tiene 0 caracteres")
        else:
            self.__nombre = otro

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, otro):
        if not isinstance(otro, str):
            raise TypeError("El apellido introducido es del tipo incorrecto")
        elif len(otro) < 0:
            raise ValueError("El apellido introducido tiene 0 caracteres")
        else:
            self.__apellido = otro

    @property
    def nota_programacion(self):
        return self.__nota_programacion
    @nota_programacion.setter
    def nota_programacion(self, otro):
        if not isinstance(otro, (int, float)):
            raise TypeError("La nota introducido es del tipo incorrecto")
        elif otro < 0 or otro > 10:
            raise ValueError("La nota introducida esta fuera de rango")
        else:
            self.__nota_programacion = otro

    @property
    def nota_algebra(self):
        return self.__nota_algebra
    @nota_algebra.setter
    def nota_algebra(self, otro):
        if not isinstance(otro, (int, float)):
            raise TypeError("La nota introducido es del tipo incorrecto")
        elif otro < 0 or otro > 10:
            raise ValueError("La nota introducida esta fuera de rango")
        else:
            self.__nota_algebra = otro

    @property
    def nota_calculo(self):
        return self.__nota_calculo
    @nota_calculo.setter
    def nota_calculo(self, otro):
        if not isinstance(otro, (int, float)):
            raise TypeError("La nota introducido es del tipo incorrecto")
        elif otro < 0 or otro > 10:
            raise ValueError("La nota introducida esta fuera de rango")
        else:
            self.__nota_calculo = otro

    @property
    def nota_fisica(self):
        return self.__nota_fisica
    @nota_fisica.setter
    def nota_fisica(self, otro):
        if not isinstance(otro, (int, float)):
            raise TypeError("La nota introducido es del tipo incorrecto")
        elif otro < 0 or otro > 10:
            raise ValueError("La nota introducida esta fuera de rango")
        else:
            self.__nota_fisica = otro

    # Métodos
    def __str__(self):
        return (f"Nombre : {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Nota Programacion: {self.nota_programacion}\n"
                f"Nota Algebra: {self.nota_algebra}\n"
                f"Nota Calculo: {self.nota_calculo}\n"
                f"Nota Física: {self.nota_fisica}\n")

nombre = input("Introduce el nombre del alumno: ")
apellido = input("Introduce el nombre del apellido: ")
nota_programacion = float(input("Introduce la nota de programacion: "))
nota_algebra = float(input("Introduce la nota de algebra: "))
nota_calculo = float(input("Introduce la nota de calculo: "))
nota_fisica = float(input("Introduce la nota de física: "))

alumno1 = Estudiante(nombre, apellido, nota_programacion, nota_algebra, nota_calculo, nota_fisica)
print(alumno1)