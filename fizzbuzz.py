"""
FizzBuzz
"""

N = 1000000

import time
def timing(f):
    def inner(*args, **kwargs):
        t0 = time.time()
        result = f(*args, **kwargs)
        print "{0:.12f}".format(time.time() - t0)
        return result
    return inner


@timing
def one_line():
    return ', '.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in xrange(1,N+1)) 


@timing
def FizzBuzz_with_generator():
    """
    FizzBuzz game using a generator
    """
    return ", ".join(str(i) for i in list(FizzBuzz_generator()))


def FizzBuzz_generator():
    """
    FizzBuzz generator
    """
    for i in range(1, N+1):
        if not i % 3 and not i % 5:
            yield "FizzBuzz"
        elif not i % 3:
            yield "Fizz"
        elif not i % 5:
            yield "Buzz"
        else:
            yield i

@timing
def FizzBuzz():
    """
    FizzBuzz game
    """

    result = []
    for i in range(1, N+1):
        if not i % 3 and not i % 5:
            result.append("FizzBuzz")
        elif not i % 3:
            result.append("Fizz")
        elif not i % 5:
            result.append("Buzz")
    return result

if __name__ == "__main__":

    print "Basic:"
    FizzBuzz()
    print "\nGenerator:"
    FizzBuzz_with_generator()
    print "\nOne line:"
    one_line()
