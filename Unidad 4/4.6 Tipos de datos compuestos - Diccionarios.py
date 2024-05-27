# Tipos de datos compuestos: Diccionarios
import json
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Imprimir el diccionario completo
print("Diccionario completo:", mi_diccionario)
print(type(mi_diccionario))
print('--------------------------------------------------------')

# Acceder a valores por clave
nombre = mi_diccionario["nombre"]
edad = mi_diccionario["edad"]

print("Nombre:", nombre)
print("Edad:", edad)
print('--------------------------------------------------------')

# Añadir o modificar un elemento
mi_diccionario["profesion"] = "Ingeniero"
print("Después de añadir 'profesion':", mi_diccionario)
print('--------------------------------------------------------')


# Eliminar un elemento
del mi_diccionario["ciudad"]
print("Después de eliminar 'ciudad':", mi_diccionario)
print('--------------------------------------------------------')

# Métodos de Diccionarios

# keys() - Obtener todas las claves del diccionario
claves = mi_diccionario.keys()
print("Claves del diccionario:", list(claves))
print('--------------------------------------------------------')

# values() - Obtener todos los valores del diccionario
valores = mi_diccionario.values()
print("Valores del diccionario:", list(valores))
print('--------------------------------------------------------')

# items() - Obtener todos los pares clave-valor del diccionario
items = mi_diccionario.items()
print("Pares clave-valor del diccionario:", list(items))
print('--------------------------------------------------------')

# get() - Obtener un valor por clave con un valor predeterminado si la clave no existe
ciudad = mi_diccionario.get("ciudad", "No especificada")
print("Ciudad:", ciudad)
print('--------------------------------------------------------')

# pop() - Eliminar un elemento por clave y devolver su valor
profesion = mi_diccionario.pop("profesion")
print("Después de pop 'profesion':", mi_diccionario)
print("Profesión eliminada:", profesion)
print('--------------------------------------------------------')

# popitem() - Eliminar y devolver el último par clave-valor
ultimo_item = mi_diccionario.popitem()
print("Después de popitem:", mi_diccionario)
print("Último par clave-valor eliminado:", ultimo_item)
print('--------------------------------------------------------')

# update() - Actualizar el diccionario con pares clave-valor de otro diccionario
mi_diccionario.update({"ciudad": "Barcelona", "pais": "España"})
print("Después de update:", mi_diccionario)
print('--------------------------------------------------------')

# clear() - Eliminar todos los elementos del diccionario
mi_diccionario.clear()
print("Después de clear:", mi_diccionario)
print('--------------------------------------------------------')

# Atributos de Diccionarios
# Los diccionarios no tienen atributos específicos, pero podemos comprobar si están vacíos y obtener su longitud

# Longitud de un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30}
longitud = len(mi_diccionario)
print("Longitud del diccionario:", longitud)
print('--------------------------------------------------------')

# Comprobación de pertenencia
tiene_clave_edad = "edad" in mi_diccionario
print("¿El diccionario tiene la clave 'edad'?:", tiene_clave_edad)
print('--------------------------------------------------------')

# Recorrer un diccionario con un bucle for
print("Recorriendo el diccionario:")
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)
print('--------------------------------------------------------')


# Ejemplos avanzados de uso de diccionarios
# Diccionarios anidados
diccionario_anidado = {
    "persona1": {"nombre": "Juan", "edad": 30},
    "persona2": {"nombre": "Ana", "edad": 25}
}
print("Diccionario anidado:", diccionario_anidado)
print('--------------------------------------------------------')

# Acceso a elementos en diccionarios anidados
print("Nombre de persona2:", diccionario_anidado["persona2"]["nombre"])
print('--------------------------------------------------------')

# Uso de diccionarios con funciones
def agregar_persona(diccionario, clave, nombre, edad):
    diccionario[clave] = {"nombre": nombre, "edad": edad}

agregar_persona(diccionario_anidado, "persona3", "Carlos", 22)
print("Después de agregar persona3:", diccionario_anidado)
print(json.dumps(diccionario_anidado, indent=4))
print('--------------------------------------------------------')
