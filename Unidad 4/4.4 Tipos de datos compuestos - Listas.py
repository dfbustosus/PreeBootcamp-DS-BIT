# Tipos de datos compuestos: Listas

# Definición de una lista
mi_lista = [1, 2, 3, 4, 5]

# Imprimir la lista completa
print("Lista completa:", mi_lista)
print(type(mi_lista))
print('--------------------------------------------------------')

# Acceder a elementos por índice
primero = mi_lista[0]   # Primer elemento
ultimo = mi_lista[-1]   # Último elemento

print("Primer elemento:", primero)
print("Último elemento:", ultimo)
print('--------------------------------------------------------')

# Slicing (segmentación) de listas
sub_lista = mi_lista[1:4]  # Elementos desde el índice 1 hasta el 3
print("Sub lista:", sub_lista)
print('--------------------------------------------------------')


# Métodos de Listas

# append() - Añadir un elemento al final de la lista
mi_lista.append(6)
print("Después de append:", mi_lista)
print('--------------------------------------------------------')

# extend() - Añadir múltiples elementos al final de la lista
mi_lista.extend([7, 8, 9])
print("Después de extend:", mi_lista)
print('--------------------------------------------------------')

# insert() - Insertar un elemento en una posición específica
mi_lista.insert(0, 0)  # Insertar 0 en la posición 0
print("Después de insert:", mi_lista)
print('--------------------------------------------------------')

# remove() - Eliminar la primera ocurrencia de un elemento
mi_lista.remove(3)
print("Después de remove:", mi_lista)
print('--------------------------------------------------------')

# pop() - Eliminar y devolver el elemento en una posición específica (por defecto, el último)
ultimo_elemento = mi_lista.pop()
print("Después de pop:", mi_lista)
print("Elemento eliminado con pop:", ultimo_elemento)
print('--------------------------------------------------------')

# index() - Devolver el índice de la primera ocurrencia de un elemento
indice_del_cuatro = mi_lista.index(4)
print("Índice del elemento 4:", indice_del_cuatro)
print('--------------------------------------------------------')

# count() - Contar las ocurrencias de un elemento
cuenta_del_dos = mi_lista.count(2)
print("Ocurrencias del elemento 2:", cuenta_del_dos)
print('--------------------------------------------------------')

# sort() - Ordenar la lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)
print('--------------------------------------------------------')

# reverse() - Invertir la lista
mi_lista.reverse()
print("Lista invertida:", mi_lista)
print('--------------------------------------------------------')

# copy() - Devolver una copia superficial de la lista
copia_lista = mi_lista.copy()
print("Copia de la lista:", copia_lista)
print('--------------------------------------------------------')

# clear() - Eliminar todos los elementos de la lista
mi_lista.clear()
print("Después de clear:", mi_lista)
print('--------------------------------------------------------')

# Atributos de Listas
# En Python, las listas no tienen atributos específicos como longitud fija, pero se pueden obtener ciertas propiedades

# Longitud de la lista
longitud = len(copia_lista)
print("Longitud de la copia de la lista:", longitud)
print('--------------------------------------------------------')

# Comprobación de pertenencia
pertenece_el_cuatro = 4 in copia_lista
print("¿El 4 está en la copia de la lista?:", pertenece_el_cuatro)
print('--------------------------------------------------------')

# Recorrer una lista con un bucle for
print("Recorriendo la copia de la lista:")
for elemento in copia_lista:
    print(elemento)
print('--------------------------------------------------------')

# Ejemplos avanzados de uso de listas
# Listas de listas (listas anidadas)
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista anidada:", lista_anidada)
print('--------------------------------------------------------')

# Acceso a elementos en listas anidadas
print("Elemento en la segunda sub-lista, tercer elemento:", lista_anidada[1][2])
print('--------------------------------------------------------')

# List comprehension - Creación de listas con expresiones concisas
cuadrados = [x**2 for x in range(10)]
print("Cuadrados de 0 a 9:", cuadrados)
print('--------------------------------------------------------')

# Ejemplo de uso en funciones
def duplicar_elementos(lista):
    return [x * 2 for x in lista]

lista_original = [1, 2, 3]
lista_duplicada = duplicar_elementos(lista_original)
print("Lista original:", lista_original)
print("Lista duplicada:", lista_duplicada)
print('--------------------------------------------------------')
