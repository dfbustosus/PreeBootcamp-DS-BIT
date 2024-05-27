# Sintaxis básica (Basic Syntax)
# Es un lenguaje dinamico tipeado que usa identacion para definir bloques de codigo

# Variables y tipos de datos
name = "Alice"      # String
age = 30            # Integer
height = 5.5        # Float
is_student = True   # Boolean

# Print 
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
print('--------------------------------------------------------')

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print('--------------------------------------------------------')
# Diccionarios
person = {
    "name": "Alice",
    "age": 30,
    "height": 5.5
}
print("Person:", person)
print('--------------------------------------------------------')
# condicionales
if age > 18:
    print(name, "is an adult.")
else:
    print(name, "is not an adult.")
print('--------------------------------------------------------')
# Loop (for)
for fruit in fruits:
    print("I like", fruit)
print('--------------------------------------------------------')
# Loop (while)
count = 0
while count < 3:
    print("Count is:", count)
    count += 1
print('--------------------------------------------------------')
# Funciones
def greet(person_name):
    print("Hello,", person_name)

greet("Alicia")
print('--------------------------------------------------------')
# Manejo de comentarios 

'''
comentario
multi linea
T
'''


# Indentación
# En Python, la identacion se usa para definir el scope de loops, functions, y condicionales.

# Ejemplo correcto
if True:
    print("This is correctly indented.")
    if True:
        print("This is also correctly indented.")
print('--------------------------------------------------------')
# Incorrecto ejemplo
# if True:
# print("This will cause an IndentationError")

