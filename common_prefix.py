strs = ["a", "ab"]

strs.sort(key=lambda x: len(x))
print strs
comm = ""

cont = True
for i, c in enumerate(strs[0]):
    if not cont:
       break
    for sttr in strs[1:]:
       if sttr[i] != c:
          cont = False
          break
    else:
        comm = comm + c

print comm
   
  
