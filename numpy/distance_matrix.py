import numpy as NP 

def distance_matrix(matrix):
	


matrix = NP.random.randint(0, 10, 12).reshape(3, 4)
dm = distance_matrix(matrix)
print dm