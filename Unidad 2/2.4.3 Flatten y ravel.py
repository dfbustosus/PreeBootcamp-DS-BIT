import numpy

a=numpy.arange(6).reshape((3,2))
print(a)
print(a.flatten(order="C"))  # Pregunta?
print(a.flatten(order="F"))  # Pregunta?


a=numpy.arange(10).reshape((5,2))
print(a)