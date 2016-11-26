meetings = [(3, 5), (0, 1), (4, 8), (10, 12), (9.5, 10)]
expected = [(0, 1), (3, 8), (9, 12)]

sorted = list(meetings)
sorted.sort()
result = [sorted[0]]

for meeting in sorted[1:]:
    previous = result[-1:][0]
    if meeting[0] >= previous[0] and meeting[0] <= previous[1] or \
       meeting[1] >= previous[0] and meeting[1] <= previous[1]:
       merged = (min(meeting[0], previous[0]), max(meeting[1], previous[1]))
       result[-1] = merged
    else:
       result.append(meeting)

free = []
for ind, meeting in enumerate(result[:-1]):
   free.append((meeting[1], result[ind+1][0]))

print sorted
print "booked:", result
print "free:", free


