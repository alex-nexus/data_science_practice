import numpy as NP 

def distance_matrix(matrix):
  r, c = matrix.shape
  return NP.sqrt(NP.sum((matrix.reshape(1, r, c) - matrix.reshape(r, 1, c))**2, axis=2))

r=1000
c=100
matrix = NP.random.randint(0, 10, r*c).reshape(r, c)
print 'matrix', matrix.shape, matrix.nbytes/1000000

dm = distance_matrix(matrix)
print 'dm:', dm.shape, dm.nbytes/1000000
print dm
