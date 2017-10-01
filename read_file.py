f = open("file", "r")
lines = 0
c = f.read(1)
while c:
  print c
  if c == '\n':
     lines += 1
  c = f.read(1)
print lines
