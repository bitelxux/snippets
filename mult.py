"""
Given list of integers, and for each index you want to find the
product of every integer except the integer at that index.
Do not use division !!

Example

Given [2, 4, 5, 6] The result should be [120, 60, 48, 40]
"""

import time

the_list = [1 + index % 4 for index in xrange(0, 20)]
expected = [7962624, 3981312, 2654208, 1990656, 7962624, 3981312,
            2654208, 1990656, 7962624, 3981312, 2654208, 1990656,
            7962624, 3981312, 2654208, 1990656, 7962624, 3981312,
            2654208, 1990656]

def timing(f):
    def inner(*args, **kwargs):
        t0 = time.time()
        result = f(*args, **kwargs)
        print time.time() - t0
        return result
    return inner

@timing
def approach1():
    """
    This approach is using substraction to mimic division.
    It has very poor perfomance, and is not able to process the
    result in a resaonable time for a list bigger than 20 elements.
    """
    result = []

    def sub_count(total, sub_num):
        count = 0
        while total != 0:
            total = total - sub_num
            count = count + 1
        return count

    total = reduce(lambda x, y: x*y, the_list)

    for a in the_list:
        result.append(sub_count(total, a))

    return result


@timing
def approach2():
    """
    This approach turns out to be much more efficient, being
    able to process a list of 5000 integers in a few seconds.
    """
    result = []
    for i in range(len(the_list)):
        lside = the_list[:i]
        rside = the_list[i+1:]

        left = lside and reduce(lambda x, y: x*y, lside) or 1
        right = rside and reduce(lambda x, y: x*y, rside) or 1

        result.append(left * right)

    return result

@timing
def approach3():
    product = 1
    """
    Thanks to Ovidiu Miron
    This approach turns out to be the best so far.
    It keeps partial multiplications in order to skip extra
    calculations ( like happens with approach2 )
    """
    output = [product]
    l = len(the_list)
    for idx in range(1, l):
        product *= the_list[idx-1]
        output.append(product)
    product = 1
    for idx in range(l-2, -1, -1):
        product *= the_list[idx+1]
        output[idx] *= product

    return output

if __name__ == "__main__":

    assert expected == approach1()
    assert expected == approach2()
    assert expected == approach3()
