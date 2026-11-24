# D=================================================================================================================== #
# Título: Ejercicio 3.	
# Crear una clase llamada Password que simbolice una contraseña, y que tenga el atributo contraseña. 
# Su constructor recibirá una cadena de caracteres y se le asignará al atributo contraseña. 
# Crear una propiedad y un setter que compruebe si la contraseña tiene mínimo 8 caracteres, al menos una mayúscula, 
# al menos una minúscula, y al menos un número.
# Autor: Miguel Jun Patricio Ferrer 
# Fecha: 24 / 11 / 26
# Version: 1.0
# D=================================================================================================================== #
class Password:
    def __init__ (self, password: str):
        self.password = password

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, otro):
        hay_mayuscula = False
        hay_minuscula = False
        hay_numero = False
        for caracter in otro:
            if caracter.isupper():
                hay_mayuscula = True
            if caracter.islower():
                hay_minuscula = True
            if caracter.isdigit():
                hay_numero = True

        if not isinstance(otro, str):
            raise TypeError("La contraseña introducida es incorrecta")
        elif len(otro) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        elif not hay_mayuscula:
            raise ValueError("La contraseña debe contener al menos una mayúscula")
        elif not hay_minuscula:
            raise ValueError("La contraseña debe contener al menos una minúscula")
        elif not hay_numero:
            raise ValueError("La contraseña debe contener al menos un número")
        else:
            self.__password = otro
        
password1 = Password("MEgusTaLaFrut4") # Funciona
# password2 = Password("doomday7") # No funciona