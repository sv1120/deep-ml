
import numpy as np
import math
def rmse(y_true, y_pred):
	# Write your code here
	diffs = np.array(y_true-y_pred)**2
	rmse_res = math.sqrt(np.mean(diffs))
	return round(rmse_res,3)
