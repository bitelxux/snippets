"""
Get the biggest product give by three numbers in a list.
"""

import itertools

LIST = [-1, -30, 3, 4, 5, 6]

def get_result():
    LIST.sort()
    three_max = LIST[-3:]
    two_min = LIST[:2]
    print three_max, two_min
    three = reduce(lambda x,y: x*y, three_max)
    two = reduce(lambda x,y: x*y, two_min)
    return max(three, two * three_max[2])

def get_result_comb():
    """
    broute force solution
    """
    maximum = 0
    combs = itertools.combinations(LIST, 3)
    for comb in combs:
        res = reduce(lambda a, b: a*b, comb)
        maximum = max(maximum, res)
    return maximum

if __name__ == "__main__":

    result = get_result()
    print result
    result = get_result_comb()
    print result
