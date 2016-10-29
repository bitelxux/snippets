def factorial_reduce(n):
    return reduce(lambda x, y: x * y, xrange(1, n+1))

def factorial_recursive(n):
    result = 1
    if n != 1:
        result = n * factorial_recursive(n - 1)
    return result
        
print factorial_recursive(5)
print factorial_reduce(5)
