# D=================================================================================================================== #
# Título: Ejercicio 4.	
# Crear una clase Dado, con campos nombre y tiradas, para simular una partida de juego de dados. 
# Crear un método init que recibe el nombre del jugador y un entero n que representa el número de tiradas 
# (debe ser mayor que cero). Asignará el nombre al campo correspondiente y creará una lista de n posiciones 
# rellena con números entre el 1 y el 6. Crear propiedades y setters. En un programa aparte se simulará una 
# partida de dados, preguntando a cada jugador su nombre y el número de tiradas del juego. 
# El ganador será el que tenga el mayor número de dados iguales. En caso de empate ganará el jugador cuyos dados sumen más.
# Autor: Miguel Jun Patricio Ferrer 
# Fecha: 24 / 11 / 26
# Version: 1.0
# D=================================================================================================================== #
import random
class Dado:
    def __init__(self, nombre: str, numero_tiradas: int):
        self.nombre = nombre
        self.numero_tiradas = numero_tiradas
        
        # Creación de la lista de las tiradas del dado
        total_tiradas = []
        for numero_dado in range(numero_tiradas):
            numero_dado = random.randint(1,6)
            total_tiradas.append(numero_dado)

        self.tiradas = total_tiradas

    # Definir las propiedades y setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, otro):
        if not isinstance(otro, str):
            raise TypeError("El nombre del jugador es del tipo incorrecto")
        elif len(otro) == 0:
            raise ValueError("El nombre introducido tiene 0 caractéres")
        else:
            self.__nombre = otro

    @property
    def numero_tiradas(self):
        return self.__numero_tiradas
    @numero_tiradas.setter
    def numero_tiradas(self, otro):
        if not isinstance(otro, int):
            raise TypeError("El número de tiradas introducido es del tipo incorrecto")
        elif otro <= 0:
            raise ValueError("El número de tiradas no puede ser negativo o 0")
        else:
            self.__numero_tiradas = otro
    @property
    def tiradas(self):
        return self.__tiradas

    @tiradas.setter
    def tiradas(self, otro):
        if not isinstance(otro, list):
            raise TypeError("El valor introducido no es una lista")
        elif 1 not in otro and 2 not in otro and 3 not in otro and 4 not in otro and 5 not in otro and 6 not in otro:
            raise ValueError("Los valores introducidos en la lista no son correctos (solo pueden ser numeros del 1 al 6)")
        else:
            self.__tiradas = otro
        

VALOR_DADO = [1, 2, 3, 4, 5, 6]
# Bucle que pide los datos de los dos jugadores
jugadores = []
numero_tiradas = int(input("Introduce el número de tiradas para la partida: ")) # Común para ambos
for i in range(2):
    nombre = input("Introduce el nombre del jugador: ")
    objeto = Dado(nombre, numero_tiradas)
    print(objeto.tiradas) # Linea de código para comprobar el código
    jugadores.append(objeto)
    

dados_iguales = [0, 0] # El primer hueco es del jugador 1, y el segundo del jugador 2
sumatorio_dados = [0, 0] # El primer hueco es del jugador 1 y el segundo del jugador 2
for i in range(len(jugadores)):
    for dado in VALOR_DADO: # Pase por los seis números, los cuente y se quede con el número más grande
        if dados_iguales[i] < jugadores[i].tiradas.count(dado):
            dados_iguales[i] = jugadores[i].tiradas.count(dado)
        sumatorio_dados[i] += jugadores[i].tiradas.count(dado) * dado # Multiplicar el valor del dado por la cantidad de veces que esta repetido

if dados_iguales[0] == dados_iguales[1]: # sumatorio y ver cual suma más
    if sumatorio_dados[0] == sumatorio_dados[1]:
        print("Empate")
    elif sumatorio_dados[0] < sumatorio_dados[1]:
        print(f"Gana {jugadores[1].nombre}")
    else:
        print(f"Gana {jugadores[0].nombre}")
elif dados_iguales[0] < dados_iguales[1]: # gana el jugador 2
    print(f"Gana {jugadores[1].nombre}")
else:
    print(f"Gana {jugadores[0].nombre}")

