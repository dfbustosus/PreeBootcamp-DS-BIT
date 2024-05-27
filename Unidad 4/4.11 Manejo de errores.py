# Manejo de Errores en Python (try-except)

def dividir_numeros(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
        return None
    except TypeError:
        print("Error: Tipos de datos no válidos para la división.")
        return None
        

# Ejemplo de uso de la función dividir_numeros con diferentes tipos de errores
print("Ejemplo 1:")
resultado = dividir_numeros(10, 2)
if resultado is not None:
    print("Resultado de la división:", resultado)

print("\nEjemplo 2:")
resultado = dividir_numeros(10, 0)  # Esto causará un ZeroDivisionError
if resultado is not None:
    print("Resultado de la división:", resultado)

print("\nEjemplo 3:")
resultado = dividir_numeros("10", 2)  # Esto causará un TypeError
if resultado is not None:
    print("Resultado de la división:", resultado)
