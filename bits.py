"""
given an integer, print the maximum bits set to 1 in a row
"""

def option1(number):
  """
  This approach converts the number to a "binary" string
  and counts the consecutive '1'
  """
  maximum = 0
  current = 0
  for bit in bin(number)[2:]:
      if bit == '1':
         current += 1
         maximum = max(maximum, current)
      else:
         maximum = max(maximum, current)
         current = 0
  return maximum 

def option2(number):
  """
  This approach use binary shift operator until the number
  becomes 0
  """
  maximum = 0
  current = 0
  while number != 0:
    if number & 1:
       current += 1
       maximum = max(maximum, current)
    else:
       maximum = max(maximum, current)
       current = 0
    number = number >> 1
  return maximum 

if __name__ == "__main__":

    number = 17061358204
    print bin(number)
    print option1(number)
    print option2(number)
   
