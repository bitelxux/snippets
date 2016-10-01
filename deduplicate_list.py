"""
Making a list with unique element from a list with duplicate elements
Iterating the list is not a desirable solution.
"""

LIST = [1, 2, 1, 1, 3, 4, 2, 5, 1, 6, 7, 2]


def deduplicate():

    print list(set(LIST))


if __name__ == "__main__":

    deduplicate()
