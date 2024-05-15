""" Set: grupo o conjunto """

# es una colección de datos que no se puede repetir y tampoco esta ordenada

PRIMER_SET = {1, 1, 2, 2, 3, 4}
print(PRIMER_SET)

SEGUNDO = [3, 4, 5]
SEGUNDO_SET = set(SEGUNDO)
print(SEGUNDO_SET)

# Los set comparten todos los metodos de las listas

# metodos extras: | = union, & = intersección - = diferencia ^ = diferencia simétrica

print("union = ", PRIMER_SET | SEGUNDO_SET)
print("intersección = ", PRIMER_SET & SEGUNDO_SET)
print("diferencia = ", PRIMER_SET - SEGUNDO_SET)
print("diferencia simétrica = ", PRIMER_SET ^ SEGUNDO_SET)

# los set no se encuentran ordenados y no es posible aceder a un elemento específico ya que no poseen in indice

# se puede averiguar si un set contiene algún elemento en particular
if 5 in SEGUNDO_SET:
    print("Elemento encontrado")
