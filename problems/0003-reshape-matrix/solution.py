import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	#check if it can be done 
	if (len(a[0])*len(a))!=new_shape[0]*new_shape[1]:
		return []
	return (np.array(a)).reshape(new_shape)