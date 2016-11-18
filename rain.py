tests = [
#([0,1,0,2,1,0,1,3,2,1,2,1], 6),
#([10,5,7,5,7], 4),
#([1,2,3,4,5,6,7,8,9], 0),
#([0,3,2,0,0,1,2,4,3,1,0,1,2,3], 18),
#([1,2,3,4,5,6,7,8], 0),
#([1,2,3,4,5,6,7,8,2,4], 2),
#([], 0),
#([1,1], 0),
#([1,1,1], 0),
#([1,2,1], 0),
#([1,0,1], 1),
#([10,1,10], 9),
#([10,1,2], 1),
#([10,2,1], 0),
#([0,1,4,3,2,1,0,1,2,3,4,3,2,1], 16),
#([0,1,4,3,2,1,0,1,2,3,4,3,2,1,2], 17),
#([1,1,1,1,1], 0),
#([7,6,5,4,3,2,1,4], 6),
#([5,4,3,2,1,0,1,0,1,0,1,0], 3),
#([5,4,3,2,1,0,1,0,1,0,3], 16),
([9,6,8,8,5,6,3], 3),
]

def _volume(A, left, right):
    vol = 0
    level = min(A[left], A[right])
    for i in xrange(left, right):
        if A[i] < level:
           vol += level - A[i]
    return vol

def rain(A):

    if len(A) < 3:
       return 0

    total = 0
    left = 0
    for i, h in enumerate(A):
        if h >= A[left]:
           right = i
           vol = _volume(A, left, right)
           total += vol
           print "%d..%d: %d" % (left, right, vol)
           left = right

    right = i
    # Adjust last section
    while A[right-1] > A[right] and right > left:
       right -= 1

    vol = _volume(A, left, right)
    total += vol
    print "%d..%d: %d" % (left, right, vol)
    return total

if __name__ == "__main__":
   for test in tests:
       total = rain(test[0]) 
       print "%s : %d" % (str(test[0]), total)
       assert total == test[1]
