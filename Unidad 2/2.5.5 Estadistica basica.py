import numpy

a=numpy.array([[5,6,1],[2,3,8]])
print(a)
print(numpy.amax(a))
print(numpy.amax(a,axis=0))
print(numpy.amax(a,axis=1))
print('----')
print(numpy.percentile(a,25))
print(numpy.percentile(a,25,axis=0))
print(numpy.percentile(a,25,axis=1))

"""
a=numpy.array([[5,6,1],[2,3,8]])
print(a)
print(numpy.amax(a))
print(numpy.amax(a,axis=0))
print(numpy.amax(a,axis=1))
print(numpy.percentile(a,25))
print(numpy.percentile(a,25,axis=0))
print(numpy.percentile(a,25,axis=1))
print(numpy.ptp(a))
print(numpy.ptp(a,axis=0))


b=numpy.array([[5,numpy.nan,1],[2,3,numpy.nan]])
print(b)
print(numpy.amin(b))
print(numpy.amax(b))
print(numpy.nanmin(b))
print(numpy.nanmin(b,axis=0))
print(numpy.nanmin(b,axis=1))
print(numpy.nanmax(b,axis=1))
print(numpy.ptp(b))
print(numpy.ptp(b,axis=0))
print(numpy.ptp(b,axis=1))
"""