def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    values.sort()
    values = values[::-1]
    if len(values) < 3:
        return values 
    else:
        return values[0:3]