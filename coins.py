import sys
import time

def timing(f):
    def inner(*args, **kwargs):
        t0 = time.time()
        result = f(*args, **kwargs)
        print "{0:.12f}".format(time.time() - t0)
        return result
    return inner

@timing
def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    row = 0
    while n>0:
       row += 1 
       n -= row

    if n < 0:
       row -= 1

    return row

@timing
def arrangeCoins2(n):
    rows = 0
    partial = 0
    for i in xrange(1, n+1):
        rows += 1
        partial += i
        if partial > n:
           return rows - 1
        if partial == n:
           return rows

@timing
def arrangeCoins3(n):
   row = 0
   cont = 0 
   while cont <= n:
       row += 1
       cont += row

   return row if cont == n else row -1

@timing
def arrangeCoins4(n):
    k = 0
    while k*(k+1)/2 <= n:
        k += 1
    return k-1

if __name__ == "__main__":
    n = int(sys.argv[1])
    print arrangeCoins(n)
    print arrangeCoins2(n)
    print arrangeCoins3(n)
    print arrangeCoins4(n)

