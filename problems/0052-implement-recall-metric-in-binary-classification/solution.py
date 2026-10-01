import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    total_positives = np.count_nonzero(y_true==1)
    true_positives_count = 0
    for i in range(len(y_true)):
        if y_true[i]==y_pred[i]==1:
            true_positives_count+=1
    return 0 if total_positives == 0 else true_positives_count/total_positives
    
