def fib(n):

    if n == 0:
       return []
    elif n == 1:
       return [0]
    elif n == 2:
       return [0, 1]

    a, b = 0, 1
    fib_list = [a, b]

    for i in xrange(0, n-2):
        fib_list.append(a+b)
        a, b = b, a+b

    return fib_list

def fib_generator(n):

    if n == 0:
       return
    elif n == 1:
       yield 0
       return
    elif n == 2:
       yield 0
       yield 1
       return

    a, b = 0, 1
    yield a
    yield b
    for i in xrange(0, n-2):
       yield a+b
       a, b = b, a+b 

for n in 0, 1, 2, 3, 10:
  print "n = {} No generator".format(n)
  result = fib(n)
  print result
  print "n = {} With generator".format(n)
  result =  list(fib_generator(n))
  print result


