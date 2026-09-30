import math
def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	sigmoid_selfgating = x/(math.exp(-x)+1)
	return round(sigmoid_selfgating, 4)