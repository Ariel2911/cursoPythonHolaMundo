""" Listas 1"""
print("LISTAS 1\n")

NUMEROS = [1, 2, 3]
LETRAS = ["A", "B", "C"]
CEROS = [0] * 10  # crear una lista con un contenido repetido n veces
ALFANUMECICO = NUMEROS+LETRAS  # une las listas
# la función list() admite como paramatro un objeto iterable y
# retorna una "lista" con cada uno de los elementos
RANGO = list(range(1, 11))
CHARS = list("Hola mundo")

print(NUMEROS)
print(LETRAS)
print(CEROS)
print(ALFANUMECICO)
print(RANGO)
print(CHARS)

# Manipulando listas
print("\nManipulando listas\n")

MASCOTAS = ["Bicho", "Pelusa", "Pulga", "Copito"]

print(MASCOTAS[1:3])  # seleciona rango de elementos.

print(MASCOTAS[-1])  # indice negativo cuenta en orden inverso

# selecionar alementos de un listado dando saltos (2)
print(MASCOTAS[::2])  # return['Bicho', 'Pulga']
print(MASCOTAS[1::2])  # return ['Pelusa', 'Copito']
print(MASCOTAS[:2:2])  # return ['Bicho']
print(MASCOTAS[1:3:2])  # return ['Pelusa']

# desempaquetado de listas
print("\nDesempaquetado de listas\n")

PRIMERO, SEGUNTO, TERCERO = NUMEROS
print(PRIMERO, SEGUNTO, TERCERO)

PRIMERO, *OTROS = LETRAS
print(PRIMERO, OTROS)

PRIMERO, *OTROS, ULTIMO = RANGO
print(PRIMERO, OTROS, ULTIMO)

# iterar listas
print("\nIterar listas\n")

# imprime los elementos
for mascota in MASCOTAS:
    print(mascota)
# imprime los elementos en forma de tuplas
for mascota in enumerate(MASCOTAS):
    print(mascota)
# desempaquetado de tuplas
for indice, mascota in enumerate(MASCOTAS):
    print(indice, mascota)


# buscar elementos dentro de listas
print("\nBuscar elementos dentro de listas\n")

# index() retorna el indice en el que se encuentra el elemento que pasamos
print("El indice de Pulga es: ", MASCOTAS.index("Pulga"))
# si el elemento que pasamos no se encuentra dentro de la lista la index() retornara un error, es por eso que debemos asegurarnos que el elemento que buscamos se encuentra dentro de la lista
if "Pipo" in MASCOTAS:
    print(MASCOTAS.index("Pipo"))
else:
    print("Elemento no encontrado")
# contar cuantos elementos determinados tenemos dentro de una lista
print(MASCOTAS.count("Pelusa"))

# agregando y eliminando elementos
print("\nAgregando y eliminando  listas\n")

# agrega el elemento en el indice indicado de la lista
MASCOTAS.insert(1, "Pipo")
print(MASCOTAS)
# agrega el elemento al final de la lista
MASCOTAS.append("Pepe")
print("append Pepe: ", MASCOTAS)

# remove() solo elimina la prinmer ocurrencia que encuentre
MASCOTAS.remove("Pepe")
print("remove Pepe: ", MASCOTAS)
# elimina el último elemento si no se le pasa como parametro ningun indice
MASCOTAS.pop()
print("pop: ", MASCOTAS)
# borrado por indice
del MASCOTAS[0]
print("del 0: ", MASCOTAS)
# borrar todos los elementos de una lista
MASCOTAS.clear()
print("clear: ", MASCOTAS)
