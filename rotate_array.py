"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

def _rotate(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

def rotate(arr, k):
    size = len(arr)
    arr = _rotate(arr, 0, size-1) 
    print arr
    arr = _rotate(arr, 0, k-1) 
    print arr
    arr = _rotate(arr, k, size-1)
    print arr

    return arr

arr = [1,2,3,4,5,6,7,8]
rotate(arr, 2) 




