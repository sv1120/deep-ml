
import numpy as np
from collections import Counter
def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	counter1 = Counter(y)
	probs0 = np.array(list(counter1.values()))
	probs = probs0* (1/len(y))
	gini =1- np.sum(probs**2)
	return gini
	return round(val,3)