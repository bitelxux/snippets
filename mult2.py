"""
Given list of integers, and for each index you want to find the
product of every integer except the integer at that index.
Do not use division !!


This is an inefficient version
"""

def sub_count(total, sub_num):
  count = 0
  while total != 0:
      total = total - sub_num
      count = count + 1
  return count

array = [1+i%4 for i in xrange(0, 40)]
total = reduce(lambda x,y: x*y, array)
results = []

for a in array:
   results.append(sub_count(total,a))

