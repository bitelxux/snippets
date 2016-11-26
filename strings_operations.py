import time

def timing(f):
    def inner(*args, **kwargs):
        t0 = time.time()
        result = f(*args, **kwargs)
        print "{0:.12f}".format(time.time() - t0)
        return result
    return inner


@timing
def first_not_repeated(input):

    all = {}
    for c in input:
        all.setdefault(c, 0)
        all[c] += 1

    for c in input:
        if all[c] == 1:
           return c

@timing
def first_not_repeated_2(input):
    """
    This is slightly slower
    """
    return sorted(c for c in input if input.count(c) == 1)[0]

@timing
def first_repeated(input):

    all = {}
    for c in input:
        all.setdefault(c, 0)
        all[c] += 1

    for c in input:
        if all[c] > 1:
           return c

@timing
def first_repeated_2(input):
    """
    This is slightly slower
    """
    return sorted(c for c in input if input.count(c) != 1)[0]

def test():
    input = "abcdefabcdefgaabcdefhijl"
    fnr = first_not_repeated(input)
    fnr2 = first_not_repeated_2(input)

    fr = first_repeated(input)
    fr2 = first_repeated_2(input)

    assert fnr == fnr2 == "g"
    assert fr == fr2 == "a"

if __name__ == "__main__":
    test()

    
