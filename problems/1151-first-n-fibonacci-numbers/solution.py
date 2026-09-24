def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    initial = [0] * n
    if n>1:     
        initial[1] = 1
    if n>2:
        for i in range(2, n):
            initial[i] = initial[i-1] + initial[i-2]
    return initial

