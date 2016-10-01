expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fib(n):
    a, b = 0, 1
    fib_list = [a, b]

    for i in xrange(0, n-2):
        fib_list.append(a+b)
        a, b = b, a+b

    return fib_list

def fib_generator(n):
    a, b = 0, 1
    yield a
    yield b
    for i in xrange(0, n-2):
       yield a+b
       a, b = b, a+b 

# without generator
result = fib(10)
print result
assert expected == result

# with generator
result =  list(fib_generator(10))
print result
assert expected == result


