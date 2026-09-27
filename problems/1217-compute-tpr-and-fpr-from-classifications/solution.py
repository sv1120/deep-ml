import numpy as np

def compute_tpr_fpr(y_true, y_pred):
    """
    Compute TPR and FPR from true and predicted binary labels.

    Args:
        y_true (array-like): Ground-truth labels (0 or 1).
        y_pred (array-like): Predicted labels (0 or 1).

    Returns:
        tuple: (tpr, fpr) as Python floats.
    """
    # TODO: compute TP, FN, FP, TN then TPR and FPR
    true_positives = 0
    false_negatives = 0
    false_positives = 0
    true_negatives = 0
    for i in range(len(y_true)):
        if y_true[i]==y_pred[i]==1:
            true_positives+=1
        if y_true[i]==y_pred[i]==0:
            true_negatives+=1
        if y_true[i] == 0 and y_pred[i]==1:
            false_positives+=1
        if y_true[i]==1 and y_pred[i]==0:
            false_negatives+=1
    tpr = 0 if (true_positives+false_negatives==0) else true_positives/(true_positives+ false_negatives)
    fpr = 0 if (true_negatives + false_positives ==0) else false_positives/(true_negatives+false_positives)
    return (tpr, fpr)
