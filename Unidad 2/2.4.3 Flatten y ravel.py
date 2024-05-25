import numpy

a=numpy.arange(6)
print(a)

b=a.reshape((3,2))
print(b)
#print(a.flatten(order="C"))  # Pregunta?
#print(a.flatten(order="F"))  # Pregunta?
print(b.flatten())

#a=numpy.arange(10).reshape((5,2))
#print(a)