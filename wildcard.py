"""
without re
"""


def matches(input, pattern):

    for index, c in enumerate(input):
        if pattern[index] == "*":
           return true
        elif pattern[index] == "?":
           continue
        elif pattern[index] == c:
           continue
        else:
           return False
