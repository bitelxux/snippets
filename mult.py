"""
Given list of integers, and for each index you want to find the
product of every integer except the integer at that index.
Do not use division !!
"""

m = [1+i%4 for i in xrange(0, 5000)]
result = []

for i in range(len(m)):
  lside = m[:i]
  rside = m[i+1:]

  left = reduce(lambda x,y: x*y, len(lside) > 1 and lside or lside + [1])
  right = reduce(lambda x,y: x*y, len(rside) > 1 and rside or rside + [1])

  #print "%d: %s %s: %d" %(i, lside, rside, left*right)
  result.append(left * right )

#print result
