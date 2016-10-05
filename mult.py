"""
Given list of integers, and for each index you want to find the
product of every integer except the integer at that index.
Do not use division !!
"""

import timeit
import time

the_list = [1+index % 4 for index in xrange(0, 20)]


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

def run_approach(approach):
    t0 = time.time()
    print approach()
    print time.time() - t0


if __name__ == "__main__":

    run_approach(approach1)
    run_approach(approach2)
