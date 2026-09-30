import numpy as np
import math

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	maxscore = max(scores)
	log_exp_normalised_sum = math.log(np.sum(np.exp(np.array([score - maxscore for score in scores]))))

	return np.array([score - maxscore - log_exp_normalised_sum for score in scores])


