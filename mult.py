"""
Given list of integers, and for each index you want to find the
product of every integer except the integer at that index.
Do not use division !!
"""

m = [1+i%4 for i in xrange(0, 3)]
result = []

for i in range(len(m)):
  lside = m[:i]
  rside = m[i+1:]

  left = lside and reduce(lambda x,y: x*y, lside) or 1
  right = rside and reduce(lambda x,y: x*y, rside) or 1

  result.append(left * right )

#print m
#print result
