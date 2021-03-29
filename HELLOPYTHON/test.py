from astropy.io.ascii.cparser import np

a = 10
print(type(a))
a = np.dtype('int64').type(a)
print(type(a))

print(a != a )