import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	n_predictions = len(y_pred)
	n_correct_pred = 0
	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i]:
			n_correct_pred+=1
	return 0 if n_predictions == 0 else n_correct_pred/n_predictions