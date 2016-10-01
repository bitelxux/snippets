import os
import sys


def walk(directory):
    """
    Walk like function
    """

    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                walk(full_path)
            else:
                print(full_path)
    except OSError, e:
        print "Oops {0}".format(e)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("process_files.py <path>")
        sys.exit(-1)

    path = sys.argv[1]
    walk(path)
