# Casting y Conversión de Datos en Python

# Casting de str a int
num_str = "10"
num_int = int(num_str)
print("Casting de str a int:", num_int)
print('--------------------------------------------------------')


# Casting de int a str
num_int = 20
num_str = str(num_int)
print("Casting de int a str:", num_str)
print('--------------------------------------------------------')

# Casting de list a tuple
mi_lista = [1, 2, 3, 4, 5]
mi_tupla = tuple(mi_lista)
print("Casting de list a tuple:", mi_tupla)
print('--------------------------------------------------------')

# Casting de tuple a list
mi_tupla = (6, 7, 8, 9, 10)
mi_lista = list(mi_tupla)
print("Casting de tuple a list:", mi_lista)
print('--------------------------------------------------------')

# Casting de list a set
mi_lista = [1, 2, 3, 4, 5, 1, 2, 3]  # Contiene duplicados
mi_set = set(mi_lista)
print("Casting de list a set:", mi_set)
print('--------------------------------------------------------')

# Casting de set a list
mi_set = {6, 7, 8, 9, 10}
mi_lista = list(mi_set)
print("Casting de set a list:", mi_lista)
print('--------------------------------------------------------')

var= 1
var2=float(var)
print(var, var2, type(var),type(var2))

var= 1.11
var2=int(var)
print(var, var2, type(var),type(var2))