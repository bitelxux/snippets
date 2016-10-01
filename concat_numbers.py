"""
Build a string with the numbers from 0 to 100, "0123456789101112..."
We may want to use str.join rather than appending a number every time.
"""


def concat_numbers():
    """
    Concat with join
    """

    print "".join(repr(n) for n in xrange(1, 101))

if __name__ == "__main__":

    concat_numbers()
