"""
FizzFuzz
"""

def fizzfuzz_with_generator():
    """
    fizzfuzz game using a generator
    """
    print ", ".join(str(i) for i in list(fizzfuzz_generator()))


def fizzfuzz_generator():
    """
    fizzfuzz generator
    """
    for i in range(1, 51):
        if not i % 3 and not i % 5:
            yield "fizzfuzz"
        elif not i % 3:
            yield "fizz"
        elif not i % 5:
            yield "fuzz"
        else:
            yield i


def fizzfuzz():
    """
    fizzfuzz game
    """

    for i in range(1, 51):
        comma = i != 50 and ", " or ""
        if not i % 3 and not i % 5:
            print "fizzfuzz{0}".format(comma),
        elif not i % 3:
            print "fizz{0}".format(comma),
        elif not i % 5:
            print "fuzz{0}".format(comma),
        else:
            print "{0}{1}".format(i, comma),

if __name__ == "__main__":

    print "Basic:"
    fizzfuzz()
    print "\nGenerator:"
    fizzfuzz_with_generator()
