import numpy as np
def precision(y_true, y_pred):
	# Your code here
	true_positives_count = 0
	positives_count = 0
	for i in range(len(y_true)):
		if y_pred[i]==1:
			positives_count+=1

	for i in range(len(y_pred)):
		if y_pred[i]==y_true[i]==1:
			true_positives_count+=1

	return 0 if positives_count == 0 else true_positives_count/positives_count

