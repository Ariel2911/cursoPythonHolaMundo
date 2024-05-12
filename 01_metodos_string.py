"""
Metodos String
"""

ANIMAL = "  ChanCHito feliz  "

print(ANIMAL.upper() + ".")
print(ANIMAL.lower() + ".")
print(ANIMAL.capitalize() + ".")
print(ANIMAL.title() + ".")
print(ANIMAL.strip() + ".")
print(ANIMAL.strip().capitalize() + ".")
print(ANIMAL.lstrip() + ".")
print(ANIMAL.rstrip() + ".")
print(ANIMAL.find("CH"))  # devuelve un indice
print(ANIMAL.find("ch"))  # devuelve un -1 si no obtiene resultado
print(ANIMAL.replace("CH", "j"))
print("nCH" in ANIMAL)  # devuelve un booleano
print("nch" in ANIMAL)  # devuelve un booleano
print("nch" not in ANIMAL)  # devuelve un booleano
