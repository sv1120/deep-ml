from collections import Counter
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	counter = Counter(apples)
	return 1-(max(counter.values())/len(apples))