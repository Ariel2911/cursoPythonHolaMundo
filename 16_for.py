"""
For
"""

# for

for numero in range(5):
    print(numero)

# for else

BUSCAR = 10

for numero in range(5):
    print(numero)
    if BUSCAR == numero:
        print("Número encontrado!!!")
        break
else:
    print("Número no encontrado")


for char in "Curso de Python":
    print(char)
