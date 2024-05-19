import numpy

a=numpy.arange(4)
print(a)
ab= a>1
print(ab)
b=numpy.ones(4,dtype=bool)
print(b)
print(ab | b)

a=numpy.arange(4)
print(a)
ab= a>1
print(ab)
b=numpy.ones(4,dtype=bool)
print(b)
print(ab & b)
print(~ab)
print(ab | b)