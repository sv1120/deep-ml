import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    denominator = sum([math.exp(score - max_score) for score in scores])
    probs = [math.exp(score - max(scores))/denominator for score in scores] 
    return probs

