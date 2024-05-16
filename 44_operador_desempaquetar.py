""" Operador desempaquetar """

LISTA = [1, 2, 3, 4]
print(LISTA)
print(*LISTA)
TUPLA = (1, 2, 3, 4)
print(TUPLA)
print(*TUPLA)

# combinar listas
LISTA2 = [5, 6,]
COMBINADA = [*LISTA, *LISTA2]
print(COMBINADA)

# desempaquetar diccionarios

PUNTO1 = {"x": 25}
PUNTO2 = {"y": 50}

NUEVO_PUNTO = {**PUNTO1, **PUNTO2, "z": 45}
print(NUEVO_PUNTO)
