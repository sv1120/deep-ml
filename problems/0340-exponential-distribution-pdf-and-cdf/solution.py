import numpy as np
import math
from collections import defaultdict
def exponential_distribution(x: list, lam: float) -> dict:
    """
    Compute exponential distribution properties.
    
    Args:
        x: Points at which to evaluate PDF and CDF
        lam: Rate parameter (lambda) of the distribution
        
    Returns:
        Dictionary with 'pdf', 'cdf', 'mean', and 'variance' keys
    """
    # Your code here
    dictionary = defaultdict(float)
    if lam <=0:
        dictionary['pdf']=None
        dictionary['cdf'] = None 
        dictionary['mean'] = None 
        dictionary['variance'] = None  
        return dict(dictionary)
    mean = round(1/lam, 4)
    variance = round(1/(lam**2), 4)
    pdfs = [0] * len(x)
    cdfs = [0] * len(x)
    for i in range(len(x)):
        if x[i]>=0:
            pdfs[i] = np.round(lam* np.exp(-lam * x[i]), 4)
            cdfs[i] = np.round(1 - np.exp(-lam * x[i]), 4)
    dictionary['pdf'] = pdfs
    dictionary['cdf'] = cdfs
    dictionary['mean'] = mean
    dictionary['variance'] = variance
    return dict(dictionary)
    

