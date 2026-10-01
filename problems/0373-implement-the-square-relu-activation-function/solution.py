import numpy as np
from collections import defaultdict
def square_relu(x: np.ndarray) -> dict:
	"""
	Apply the Square ReLU activation function and compute its derivative.
	
	Args:
		x: Input numpy array of any shape
	
	Returns:
		Dictionary with 'output' and 'derivative' as numpy arrays
	"""
	values = np.where(x>0,np.round(x**2, 2), 0)
	derivs = np.where(x>0, np.round(2*x, 2), 0)

	dictionary = defaultdict(float)
	dictionary['output'] = values
	dictionary['derivative'] = derivs
	return dict(dictionary)