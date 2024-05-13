"""
Funciones
"""

# función con parametros que tienen un valor por defecto


def info(nombre, edad="55"):
    print(f"Tu nombre es {nombre} y tu edad es {edad}")


info("Ariel", "65")
# argumentos nombrados
info(edad="95", nombre="Ariel")


def suma(a, b):
    print(a+b)


suma(2, 5)

# función que empaqueta en un iterable los n parametros que recive


def sumaMultipleArg(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


sumaMultipleArg(2, 5)
sumaMultipleArg(2, 5, 3)

# keyword argumets.
# función que empaqueta en un diccionario los n parametros que recive


def get_prodcut(**data):
    print(data["id"], data["name"], data["description"])


get_prodcut(
    id="23",
    name="mouse",
    description="descripción del producto"
)
