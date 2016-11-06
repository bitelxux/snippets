"""
FizzBuzz
"""

def one_line():
    print ', '.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in xrange(1,51)) 


def FizzBuzz_with_generator():
    """
    FizzBuzz game using a generator
    """
    print ", ".join(str(i) for i in list(FizzBuzz_generator()))


def FizzBuzz_generator():
    """
    FizzBuzz generator
    """
    for i in range(1, 51):
        if not i % 3 and not i % 5:
            yield "FizzBuzz"
        elif not i % 3:
            yield "Fizz"
        elif not i % 5:
            yield "Buzz"
        else:
            yield i


def FizzBuzz():
    """
    FizzBuzz game
    """

    for i in range(1, 51):
        comma = i != 50 and ", " or ""
        if not i % 3 and not i % 5:
            print "FizzBuzz{0}".format(comma),
        elif not i % 3:
            print "Fizz{0}".format(comma),
        elif not i % 5:
            print "Buzz{0}".format(comma),
        else:
            print "{0}{1}".format(i, comma),

if __name__ == "__main__":

    print "Basic:"
    FizzBuzz()
    print "\nGenerator:"
    FizzBuzz_with_generator()
    print "\nOne line:"
    one_line()
