""" Diccionarios """

# Son una colección de datos que se encuentran agrupados por una llave: valor

PUNTOS = {"x": 25, "y": 50}

print(PUNTOS)
print(PUNTOS["x"])

# si intentamos acceder a una llave que no exsista python nos lanzara un error
# para evitar esto debemos asugurarnos que exista para utilizarlo

if "x" in PUNTOS:
    print("Llave encontrada: ", PUNTOS["x"])
else:
    print("Llave no encontrada")

if "la" in PUNTOS:
    print("Llave encontrada: ", PUNTOS["la"])
else:
    print("Llave no encontrada")

# método get()
print(PUNTOS.get("y"))
print(PUNTOS.get("la", "Llave no encontrada"))

# agregar llaves
PUNTOS["z"] = 45
print(PUNTOS)

# eliminar llaves
print("\neliminar llaves\n")

del PUNTOS["y"]
print(PUNTOS)

del (PUNTOS["x"])
print(PUNTOS)

PUNTOS["x"] = 25

# acceder a los diccionarios
print("\nacceder a los diccionarios\n")

for llave in PUNTOS:
    print("llave: ", llave)
    print("valor: ", PUNTOS[llave])

for valor in PUNTOS.items():
    print(valor)

for llave, valor in PUNTOS.items():
    print("llave: ", llave)
    print("valor: ", valor)

# iteración de una lista de diccionarios
print("\niteración de una lista de diccionarios\n")

MASCOTAS = [
    {
        "id": 1,
        "nombre": "Bicho"
    },
    {
        "id": 2,
        "nombre": "Pelusa"
    },
    {
        "id": 3,
        "nombre": "Pulga"
    },
    {
        "id": 4,
        "nombre": "Copito"
    }
]


for mascotas in MASCOTAS:
    print(mascotas["nombre"])
