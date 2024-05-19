import numpy

a=numpy.array([[1,2],[3,4]])
print(a)
print(a.shape)
print('--')
b=numpy.array([[5,6]]) # OJO
print(b)
print(b.shape)
print('----')
print(numpy.concatenate((a,b),axis=0)) # Pegado por filas
print(numpy.concatenate((a,b.T),axis=1)) # Pegado por columns


a=numpy.array([[1,2],[3,4]])
print(a)
print(a.shape)
print('--')
b=numpy.array([[5,6]]) # OJO
print(b)
print(b.shape)
print('----')
print(numpy.concatenate((a,b),axis=0)) # Pegado por filas
print(b.T.shape)
print(numpy.concatenate((a,b.T),axis=1)) # Pegado por columns


a=numpy.array([2,3,4])
print(a)
print(a.shape)
print('----------')
b=numpy.array([[1,2,3],[2,3,4]])
print(b)
print(b.shape)
print('-------')
a+b