results = []

def sub_count(total, sub_num):
  count = 0
  while total != 0:
      total = total - sub_num
      count = count + 1
  return count

array = [1+i%4 for i in xrange(0, 40)]
total = reduce(lambda x,y: x*y, array)
#print 'total ',total
#print '------'

for a in array:
   results.append(sub_count(total,a))

#print array
#print results
