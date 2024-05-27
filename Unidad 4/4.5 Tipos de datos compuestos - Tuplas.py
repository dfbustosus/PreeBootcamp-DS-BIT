# Tipos de datos compuestos: Tuplas

# Definición de una tupla
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla2= tuple([1,2])

# Imprimir la tupla completa
print("Tupla completa:", mi_tupla)
print("Tupla completa2:", mi_tupla2)
print('--------------------------------------------------------')

# Acceder a elementos por índice
primero = mi_tupla[0]   # Primer elemento
ultimo = mi_tupla[-1]   # Último elemento

print("Primer elemento:", primero)
print("Último elemento:", ultimo)
print('--------------------------------------------------------')

# Slicing (segmentación) de tuplas
sub_tupla = mi_tupla[1:4]  # Elementos desde el índice 1 hasta el 3
print("Sub tupla:", sub_tupla)
print('--------------------------------------------------------')

# Métodos de Tuplas

# count() - Contar las ocurrencias de un elemento
cuenta_del_dos = mi_tupla.count(4)
print("Ocurrencias del elemento 2:", cuenta_del_dos)
print('--------------------------------------------------------')

# index() - Devolver el índice de la primera ocurrencia de un elemento
indice_del_cuatro = mi_tupla.index(4)
print("Índice del elemento 4:", indice_del_cuatro)
print('--------------------------------------------------------')

# Atributos de Tuplas
# Las tuplas son inmutables y no tienen métodos como append() o remove(), pero se pueden obtener ciertas propiedades.

# Longitud de una tupla
longitud = len(mi_tupla)
print("Longitud de la tupla:", longitud)
print('--------------------------------------------------------')

# Comprobación de pertenencia
pertenece_el_cuatro = 4 in mi_tupla
print("¿El 4 está en la tupla?:", pertenece_el_cuatro)
print('--------------------------------------------------------')

# Recorrer una tupla con un bucle for
print("Recorriendo la tupla:")
for elemento in mi_tupla:
    print(elemento)
print('--------------------------------------------------------')

# Ejemplos avanzados de uso de tuplas
# Desempaquetado de tuplas
a, b, c, d, e = mi_tupla
print("Desempaquetado de tupla:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print('--------------------------------------------------------')

# Tuplas anidadas
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print('--------------------------------------------------------')

# Acceso a elementos en tuplas anidadas
print("Elemento en la primera sub-tupla, segundo elemento:", tupla_anidada[0][1])
print('--------------------------------------------------------')

# Funciones que devuelven múltiples valores usando tuplas
def min_max(datos):
    return min(datos), max(datos)

datos = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
minimo, maximo = min_max(datos)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print('--------------------------------------------------------')

# Convertir entre listas y tuplas
mi_lista = [1, 2, 3]
mi_tupla_desde_lista = tuple(mi_lista)
print("Tupla desde lista:", mi_tupla_desde_lista)
print('--------------------------------------------------------')

lista_desde_tupla = list(mi_tupla)
print("Lista desde tupla:", lista_desde_tupla)
print('--------------------------------------------------------')
