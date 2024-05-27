# Tipos de datos compuestos: Sets (Conjuntos)

# Definición de un set
mi_set = {1, 2, 3, 4, 5}

# Imprimir el set completo
print("Set completo:", mi_set)
print('--------------------------------------------------------')

# Añadir un elemento
mi_set.add(6)
print("Después de añadir 6:", mi_set)
print('--------------------------------------------------------')

# Añadir múltiples elementos
mi_set.update([7, 8, 9])
print("Después de añadir [7, 8, 9]:", mi_set)
print('--------------------------------------------------------')

# Eliminar un elemento (si existe)
mi_set.discard(3)
print("Después de descartar 3:", mi_set)
print('--------------------------------------------------------')

# Eliminar un elemento (con error si no existe)
mi_set.remove(2)
print("Después de remover 2:", mi_set)
print('--------------------------------------------------------')

# Eliminar un elemento arbitrario
elemento_eliminado = mi_set.pop()
print("Después de pop:", mi_set)
print("Elemento eliminado:", elemento_eliminado)
print('--------------------------------------------------------')

# Limpiar el set
mi_set.clear()
print("Después de clear:", mi_set)
print('--------------------------------------------------------')

# Métodos de Sets

# Definir dos sets para operaciones
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Unión de sets
union_set = set_a.union(set_b)
print("Unión de set_a y set_b:", union_set)
print('--------------------------------------------------------')

# Intersección de sets
interseccion_set = set_a.intersection(set_b)
print("Intersección de set_a y set_b:", interseccion_set)
print('--------------------------------------------------------')

# Diferencia de sets
diferencia_set = set_a.difference(set_b)
print("Diferencia de set_a y set_b:", diferencia_set)
print('--------------------------------------------------------')

# Diferencia simétrica de sets
diferencia_simetrica_set = set_a.symmetric_difference(set_b)
print("Diferencia simétrica de set_a y set_b:", diferencia_simetrica_set)
print('--------------------------------------------------------')

# Atributos y operaciones adicionales de Sets

# Longitud de un set
longitud = len(set_a)
print("Longitud de set_a:", longitud)
print('--------------------------------------------------------')

# Comprobación de pertenencia
pertenece_el_tres = 3 in set_a
print("¿El 3 está en set_a?:", pertenece_el_tres)
print('--------------------------------------------------------')
print('--------------------------------------------------------')

# Subconjunto
es_subconjunto = {1, 2}.issubset(set_a)
print("{1, 2} es subconjunto de set_a:", es_subconjunto)
print('--------------------------------------------------------')

# Superconjunto
es_superconjunto = set_a.issuperset({1, 2})
print("set_a es superconjunto de {1, 2}:", es_superconjunto)
print('--------------------------------------------------------')

# Conjunto disjunto
es_disjunto = set_a.isdisjoint({5, 6})
print("set_a es disjunto de {5, 6}:", es_disjunto)
print('--------------------------------------------------------')

# Recorrer un set con un bucle for
print("Recorriendo set_a:")
for elemento in set_a:
    print(elemento)
print('--------------------------------------------------------')

# Ejemplos avanzados de uso de sets
# Eliminación de duplicados de una lista usando sets
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
set_sin_duplicados = set(lista_con_duplicados)
print("Lista sin duplicados:", set_sin_duplicados)
print('--------------------------------------------------------')

# Convertir de vuelta a lista si es necesario
lista_sin_duplicados = list(set_sin_duplicados)
print("Lista sin duplicados (convertida de nuevo a lista):", lista_sin_duplicados)
print('--------------------------------------------------------')
