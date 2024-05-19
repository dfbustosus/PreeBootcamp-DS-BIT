import numpy
a=numpy.arange(1,11,1)
print(a)
print('----')
print(a[1],a[-1])
print('----')
print(a[3:-4])
print(a[0:9:2])
type(a[[3,5]])
# Al extraer varios elementos de un array se genera otro array 