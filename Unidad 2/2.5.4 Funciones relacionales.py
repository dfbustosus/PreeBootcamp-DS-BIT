import numpy

"""
a=numpy.arange(4)
b=numpy.array([0,1,2.2,3.1])
print(numpy.allclose(a,b,atol=0.25))
print(numpy.allclose(a,b,atol=0.15))
c=numpy.array([[False,False],[True,True]])
print(c)
print(numpy.all(c,axis=0))
print(numpy.all(c,axis=1))
"""


a=numpy.arange(4)
b=numpy.array([0,1,2.1,3.0])
print('a: ',a)
print('b: ',b)
print(numpy.array_equal(a,b))
print(numpy.greater(a,b))
print(numpy.greater_equal(a,b))
print(numpy.less(a,b))
print(numpy.less_equal(a,b))
print(numpy.equal(a,b))
print(numpy.not_equal(a,b))
