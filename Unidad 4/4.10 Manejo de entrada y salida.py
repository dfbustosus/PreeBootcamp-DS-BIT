# Manejo de Entrada y Salida en Python

# Utilizando print para mostrar información en la consola
print("Bienvenido al programa de manejo de entrada y salida en Python")
print("Por favor, ingresa tu nombre:")

# Utilizando input para recibir entrada del usuario
nombre = input("Aqui ingresa tu nombre:")
print(f"El nombre de la persona ingresada es: {nombre} y su tipo de dato es {type(nombre)}")

# Mostrando un mensaje con el nombre ingresado
print("Hola,", nombre, "! Gracias por usar este programa.")

# Solicitando al usuario que ingrese un número
print("Por favor, ingresa un número entero:")

# Utilizando input para recibir un número del usuario (como cadena)
numero_str = input()

# Convirtiendo la cadena a un número entero utilizando int()
numero_int = int(numero_str)

# Realizando una operación simple con el número ingresado
resultado = numero_int * 2

# Mostrando el resultado al usuario
print("El doble del número que ingresaste es:", resultado)

# Finalizando el programa
print("Gracias por utilizar este programa. ¡Hasta luego!")

entrada= input("Ingresa tu salario incluyendo decimales: ")
try:
    salario=float(entrada)
    print(f"Tu salario mas intereses es de {round(salario*1.10,2)}")
except:
    print("Te equivocaste ingresa un numero")
