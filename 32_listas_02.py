""" Listas 2"""
print("LISTAS 2")

# ordenar listas
print("\nOrdenar listas\n")

NUMEROS_RANDOM = [2, 4, 1, 45, 74, 22]
MASCOTAS = [[4, "Bicho"], [1, "Pelusa"], [5, "Pulga"]]
MASCOTAS2 = [["Bicho", 4], ["Pelusa", 1], ["Pulga", 5]]

# ordena una lista
NUMEROS_RANDOM.sort()
print(NUMEROS_RANDOM)
#
MASCOTAS.sort()
print(MASCOTAS)
MASCOTAS2.sort()
print(MASCOTAS2)


# def ordena(elemento):
#     return elemento[1]
# MASCOTAS2.sort(key=ordena)
# print(MASCOTAS2)
MASCOTAS2.sort(key=lambda el: el[1])
print("sort-lambda", MASCOTAS2)

# orden invertido de una lista
NUMEROS_RANDOM.sort(reverse=True)
print("orden invertido", NUMEROS_RANDOM)

# sorted()
NUMEROS_RANDOM = [2, 4, 1, 45, 74, 22]

# ordena y devuelve una nueva lista
NUMEROS_RANDOM2 = sorted(NUMEROS_RANDOM)
print(NUMEROS_RANDOM2)

# orden invertido de una lista
NUMEROS_RANDOM2 = sorted(NUMEROS_RANDOM, reverse=True)
print("orden invertido", NUMEROS_RANDOM2)

# compresión de listas
print("\nCompresión de listas\n")

# transformación (map)
NOMBRES = [mascota[0] for mascota in MASCOTAS2]
print(NOMBRES)
NOMBRES = list(
    map(lambda mascota: mascota[0], MASCOTAS2)
)
print("map()", NOMBRES)


# filtrar (filter)
NOMBRES = [mascota for mascota in MASCOTAS2 if mascota[1] > 2]
print(NOMBRES)
NOMBRES = list(
    filter(lambda mascota: mascota[1] > 2, MASCOTAS2)
)
print("filter()", NOMBRES)

# filtrar y transformar
NOMBRES = [mascotas[0] for mascotas in MASCOTAS2 if mascotas[1] > 2]
print(NOMBRES)
NOMBRES = list(
    map(
        lambda mascota: mascota[0],
        filter(lambda mascotas2: mascotas2[1] > 2, MASCOTAS2)
    )
)
print("map(), filter()", NOMBRES)
