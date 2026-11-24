# D=================================================================================================================== #
# Título: Ejercicio 1.	
# Crear una clase llamada CuentaBancaria que tendrá los siguientes atributos: titular y cantidad 
# (puede tener decimales). Crear un constructor que reciba el nombre del titular e inicialice la cantidad a 0. 
# Crear propiedades y setters para comprobar que los valores son correctos. Lanzar excepciones cuando sea necesario.
# Autor: Miguel Jun Patricio Ferrer 
# Fecha: 24 / 11 / 26
# Version: 1.0
# D=================================================================================================================== #
class CuentaBancaria:
    
    # Definir los atributos de la clase
    def __init__(self, titular: str):
        self.titular = titular
        self.cantidad = 0

    # Definir las propiedades y setters
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, otro):
        if not isinstance(otro, str):
            raise TypeError("El nombre del titular es del tipo incorrecto")
        elif len(otro) < 0:
            raise ValueError("El nombre introducido tiene 0 caractéres")
        else:
            self.__titular = otro

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, otro):
        if not isinstance(otro, (int, float)):
            raise TypeError("La cantidad introducida es del tipo incorrecto")
        elif otro < 0:
            raise ValueError("La cantidad introducida es negativa")
        else:
            self.__cantidad = otro

# Código de prueba
cuenta1 = CuentaBancaria("MarcoAurelio")
cuenta1.cantidad = 100
print(cuenta1.cantidad)