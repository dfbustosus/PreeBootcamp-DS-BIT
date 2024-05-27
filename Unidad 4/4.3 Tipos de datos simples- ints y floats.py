# Tipos de datos simples: Ints y Floats

# Definición de Ints y Floats
entero = 10            # Tipo de dato entero (int)
flotante = 10.5        # Tipo de dato de punto flotante (float)

print("Entero:", entero)
print("Flotante:", flotante)
print('--------------------------------------------------------')

# Operaciones Básicas

# Suma
suma = entero + flotante
print("Suma:", suma)
print('--------------------------------------------------------')
# Resta
resta = entero - flotante
print("Resta:", resta)
print('--------------------------------------------------------')
# Multiplicación
multiplicacion = entero * flotante
print("Multiplicación:", multiplicacion)
print('--------------------------------------------------------')
# División
division = entero / flotante
print("División:", division)
print('--------------------------------------------------------')
# División entera
division_entera = entero // 3
print("División entera:", division_entera)
print('--------------------------------------------------------')
# Módulo (resto de la división)
modulo = entero % 3
print("Módulo:", modulo)
print('--------------------------------------------------------')
# Potencia
potencia = entero ** 2
print("Potencia:", potencia)
print('--------------------------------------------------------')

# Jerarquía de Operaciones (PEMDAS)
# Paréntesis, Exponentes, Multiplicación/División (de izquierda a derecha), Adición/Sustracción (de izquierda a derecha)

# Ejemplo de jerarquía de operaciones
resultado = (2 + 3) * 2 ** 2 / 2 -3
# Desglose:
# Paréntesis: (2 + 3) -> 5
# Exponentes: 2 ** 2 -> 4
# Multiplicación/División: 5 * 4 / 2 -> 20 / 2 -> 10
# Sustracción: 10 - 3 -> 7
print("Resultado de la operación:", resultado)
print('--------------------------------------------------------')

# Convertir entre tipos de datos
# Convertir int a float
convertido_a_float = float(entero)
print("Convertido a float:", convertido_a_float)
print('--------------------------------------------------------')
# Convertir float a int (esto trunca el número, no redondea)
convertido_a_int = int(flotante)
print("Convertido a int:", convertido_a_int)
print('--------------------------------------------------------')

# Funciones Matemáticas Adicionales
import math
# Raíz cuadrada
raiz_cuadrada = math.sqrt(entero)
print("Raíz cuadrada:", raiz_cuadrada)
print('--------------------------------------------------------')
# Valor absoluto
valor_absoluto = abs(-entero)
print("Valor absoluto:", valor_absoluto)
print('--------------------------------------------------------')
# Redondeo
redondeo = round(flotante)
print("Redondeo:", redondeo)
print('--------------------------------------------------------')
# Redondeo con número de decimales especificado
redondeo_dos_decimales = round(flotante, 2)
print("Redondeo a dos decimales:", redondeo_dos_decimales)
print('--------------------------------------------------------')
# Máximo y Mínimo
maximo = max(entero, flotante)
minimo = min(entero, flotante)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print('--------------------------------------------------------')
"""
# Ejemplo avanzado con funciones y operaciones
def operaciones_avanzadas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a ** b
    return suma, resta, multiplicacion, division, potencia

a, b = 7, 2.5
resultados = operaciones_avanzadas(a, b)
print(f"Operaciones avanzadas con {a} y {b}:")
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])
print("Potencia:", resultados[4])
print('--------------------------------------------------------')
# Uso de math para otras operaciones matemáticas avanzadas
# Logaritmo
logaritmo = math.log(entero)
print("Logaritmo:", logaritmo)
print('--------------------------------------------------------')
# Constantes
pi = math.pi
print("Valor de Pi:", pi)
print('--------------------------------------------------------')
e = math.e
print("Valor de e:", e)
print('--------------------------------------------------------')
"""