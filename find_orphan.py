"""
Get the not repeated id in a list with pairs
"""

LIST = [1, 2, 3, 3, 2, 4, 1, 5, 6, 5, 6]


def get_orphan():

    orphan_id = 0

    for item in LIST:
        orphan_id ^= item

    return orphan_id

if __name__ == "__main__":

    orphan =  get_orphan()
    print orphan
