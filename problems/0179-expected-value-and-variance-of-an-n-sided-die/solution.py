def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	expected = (n+1)/2
	expected_squared = (n* (n+1) * ((2 * n) +1))/6
	variance = (1/n * expected_squared) - expected**2
	return [expected, variance]
