def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    from collections import defaultdict
    ranking_dict = defaultdict(int)
    
    for item in order:
        ranking_dict[item] = order.index(item)
    
    return [ranking_dict[item] if item in order else -1 for item in values]