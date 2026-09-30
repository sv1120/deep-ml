import numpy as np
import math
def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	array1 = np.array(v1)
	array2 = np.array(v2)
	dotproduct = np.dot(array1, array2)
	mag_vec1 = math.sqrt(np.dot(v1, v1))
	mag_vec2 = math.sqrt(np.dot(v2, v2))
	result = dotproduct/(mag_vec1*mag_vec2)
	return round(result, 3)