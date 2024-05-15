""" Tuplas """

NUMEROS = (1, 2, 3)
print(NUMEROS)
NUMEROS = (1, 2, 3) + (4, 5, 6)
print(NUMEROS)

NUMEROS = tuple([1, 2, 3, 4, 5, 6])
print(NUMEROS)
LETRAS = tuple("Hola mundo")
print(LETRAS)

# Las tuplas comparten todos los metodos de las listas menos los que se utilizan para modificarlas
# *OTROS es una lista que contiene todos los elementos sobrantes
PRIMERO, SEGUNDO, *OTROS = NUMEROS
print(PRIMERO, SEGUNDO, OTROS)

# modificar los elementos de una tupla

NUMEROS_modificados = list(
    map(lambda numeros2: numeros2*2, NUMEROS)
)
print(NUMEROS_modificados)
