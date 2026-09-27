import numpy as np

def make_diagonal(x):
	# Your code here
	n = len(x)
	matrix = np.zeros((n, n))
	for i in range(n):
		matrix[i,i] = x[i]
	return matrix