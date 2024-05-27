# Tipo de dato booleano (bool)

# Definición de booleanos
es_verdadero = True
es_falso = False

print("Valor de es_verdadero:",es_verdadero)
print("Valor de es_falso:", es_falso)
print('--------------------------------------------------------')

# Comparaciones que devuelven booleanos
a = 10
b = 20

# Comparaciones
print("a == b:", a == b)     # Igualdad
print("a != b:", a != b)     # Desigualdad
print("a > b:", a > b)       # Mayor que
print("a < b:", a < b)       # Menor que
print("a >= b:", a >= b)     # Mayor o igual que
print("a <= b:", a <= b)     # Menor o igual que
print('--------------------------------------------------------')

# Operaciones lógicas
verdadero_y_falso = es_verdadero and es_falso
print("True and False:", verdadero_y_falso)
print('--------------------------------------------------------')

verdadero_o_falso = es_verdadero or es_falso
print("True or False:", verdadero_o_falso)
print('--------------------------------------------------------')

no_verdadero = not es_verdadero
print("not True:", no_verdadero)
print('--------------------------------------------------------')

# Métodos y usos de booleanos

# Uso de booleanos en estructuras de control
if es_verdadero:
    print("Esto se imprimirá porque es_verdadero es True")

if not es_falso:
    print("Esto se imprimirá porque es_falso es False y not False es True")
print('--------------------------------------------------------')

# Booleanos a partir de otros tipos de datos
print("bool(0):", bool(0))       # Falso
print("bool(1):", bool(1))       # Verdadero
print("bool(42):", bool(42))     # Verdadero
print('--------------------------------------------------------')

print("bool(''):", bool(''))     # Falso
print("bool('Hola'):", bool('Hola')) # Verdadero
print('--------------------------------------------------------')

print("bool([]):", bool([]))     # Falso
print("bool([1, 2, 3]):", bool([1, 2, 3])) # Verdadero
print('--------------------------------------------------------')

print("bool(None):", bool(None)) # Falso
print('--------------------------------------------------------')

# Ejemplo avanzado: Filtros con booleanos
numeros = [0, 1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)
print('--------------------------------------------------------')

# Booleanos en funciones
def es_par(n):
    return n % 2 == 0

print("¿4 es par?:", es_par(4))
print("¿7 es par?:", es_par(7))
print('--------------------------------------------------------')

# Comparaciones encadenadas
x = 5
print("1 < x < 10:", 1 < x < 10)   # True
print('--------------------------------------------------------')

# Uso de booleanos con listas de comprensión
pares = [num for num in numeros if num % 2 == 0]
print("Números pares con lista de comprensión:", pares)
print('--------------------------------------------------------')

# Uso de any() y all()
lista_booleana = [True, False, True]
print("any(lista_booleana):", any(lista_booleana))  # True si al menos un elemento es True
print("all(lista_booleana):", all(lista_booleana))  # True si todos los elementos son True
print('--------------------------------------------------------')

# Ejemplo con any() y all()
numeros_mayores_que_dos = [n > 2 for n in numeros]
print("Números mayores que dos:", numeros_mayores_que_dos)
print("¿Algún número mayor que dos?:", any(numeros_mayores_que_dos))
print("¿Todos los números mayores que dos?:", all(numeros_mayores_que_dos))
print('--------------------------------------------------------')
