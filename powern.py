"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""

from math import sqrt
import sys

def is_power_of_4(m):

    if m <= 0:
       return False

    bin_repr = bin(m)[2:]
    if bin_repr.count('0') % 2 != 0:
       return False

    nbits = len(bin_repr)
    mask = 1 << nbits - 1
    return m | mask == mask

if __name__ == "__main__":
   m = int(sys.argv[1])
    
   print is_power_of_4(m)
