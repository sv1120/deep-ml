
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	ssr = np.sum((np.array(y_pred) - np.array(y_true))**2)
	mean_true = np.mean(y_true)
	sst = np.sum((np.array(y_true) - mean_true)**2)
	return 1-(ssr/sst)