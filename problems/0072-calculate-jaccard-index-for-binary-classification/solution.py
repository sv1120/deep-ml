
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	if len(y_true)==0 and len(y_pred)==0:
		return 0
	union = 0
	intersection = 0
	for i in range(len(y_true)):
		if y_true[i]==y_pred[i]==1:
			intersection+=1
		if y_true[i] ==1 or y_pred[i]==1:
			union+=1
	result = intersection/union

	return round(result, 3)
