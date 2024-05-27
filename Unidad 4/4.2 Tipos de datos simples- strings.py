# Tipos de datos simples: Strings
mi_string = "Hola, mundo!"

# Indexación de Strings
# Los índices empiezan en 0
primera_letra = mi_string[0]
ultima_letra = mi_string[-1]

print("String completo:", mi_string)
print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)
print('--------------------------------------------------------')

# Slicing (segmentación) de Strings
sub_string = mi_string[0:4]  # Obtiene caracteres desde el índice 0 hasta el 3
print("Sub string:", sub_string)
print('--------------------------------------------------------')
# Métodos de Strings
# Los métodos son funciones que pertenecen a un objeto y se llaman usando el operador de punto (.)

# Cambiar a mayúsculas
mayusculas = mi_string.upper()
print("Mayúsculas:", mayusculas)
print('--------------------------------------------------------')
# Cambiar a minúsculas
minusculas = mi_string.lower()
print("Minúsculas:", minusculas)
print('--------------------------------------------------------')
# Capitalizar (primer letra en mayúscula)
capitalizado = mi_string.capitalize()
print("Capitalizado:", capitalizado)
print('--------------------------------------------------------')

# Contar la cantidad de veces que un substring aparece
contar_o = mi_string.count('o')
print("Cantidad de 'o' en el string:", contar_o)
print('--------------------------------------------------------')

# Encontrar la posición de un substring
posicion_mundo = mi_string.find('mundo')
print("Posición de 'mundo':", posicion_mundo)
print('--------------------------------------------------------')

# Reemplazar una parte del string
nuevo_string = mi_string.replace('mundo', 'Python')
print("Nuevo string:", nuevo_string)
print('--------------------------------------------------------')

# Comprobar si todos los caracteres son alfanuméricos
es_alfanumerico = mi_string.isalnum()  # Falso porque hay signos de puntuación y espacios
print("Es alfanumérico:", es_alfanumerico)
print('--------------------------------------------------------')
# Comprobar si todos los caracteres son letras
es_alpha = mi_string.isalpha()  # Falso por los espacios y signos de puntuación
print("Es alfabético:", es_alpha)
print('--------------------------------------------------------')
# Comprobar si todos los caracteres son dígitos
solo_digitos = "12345".isdigit()
print("Solo dígitos:", solo_digitos)
print('--------------------------------------------------------')
# Longitud de un string
longitud = len(mi_string)
print("Longitud del string:", longitud)
print('--------------------------------------------------------')
# Dividir un string en una lista
lista_palabras = mi_string.split()
print("Lista de palabras:", lista_palabras)
print('--------------------------------------------------------')

# Unir una lista en un string
unido = " ".join(lista_palabras)
print("String unido:", unido)
print('--------------------------------------------------------')

# Atributos de Strings
# En Python, los strings no tienen atributos específicos como los objetos en otros lenguajes, 
# pero puedes acceder a sus métodos utilizando el operador de punto como se mostró anteriormente.

# Ejemplos avanzados

# Formateo de Strings
nombre = "Juan"
edad = 28

# Usando f-strings
saludo = f"Hola, {nombre}. Tienes {edad} años."
print("Saludo con f-string:", saludo)
print('--------------------------------------------------------')

# Usando el método format
saludo_format = "Hola, {}. Tienes {} años.".format(nombre, edad)
print("Saludo con format:", saludo_format)
print('--------------------------------------------------------')

# Usando el operador %
saludo_porcentaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print("Saludo con %:", saludo_porcentaje)
print('--------------------------------------------------------')
print('--------------------------------------------------------')

# Comparación de Strings
string1 = "Hola"
string2 = "hola"
comparacion = string1 == string2  # Falso, Python es sensible a mayúsculas y minúsculas
print("Comparación de strings:", comparacion)
print('--------------------------------------------------------')
# Convirtiendo otros tipos de datos a string
numero = 123
numero_como_string = str(numero)
print("Número como string:", numero_como_string)
print('--------------------------------------------------------')
