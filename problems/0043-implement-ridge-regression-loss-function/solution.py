import torch

def ridge_loss(X: torch.Tensor, w: torch.Tensor, y_true: torch.Tensor, alpha: float) -> torch.Tensor:
    """
    Implements the Ridge Regression Loss Function using PyTorch.
    
    Args:
        X: Feature matrix of shape (n_samples, n_features)
        w: Weight vector of shape (n_features,)
        y_true: True target values of shape (n_samples,)
        alpha: Regularization parameter (lambda)
    
    Returns:
        The Ridge loss value as a scalar tensor
    """
    # Your implementation here
    # first calculate beta vector 
    penalty_term = (alpha * torch.sum(w**2)).item()
    mse = (1/len(y_true))*torch.sum((X @ w - y_true)**2).item()
    return mse + penalty_term

