"""
given an integer, print the maximum bits in a row set to 1
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
       current = 0
    number = number >> 1
  return maximum 

if __name__ == "__main__":

    number = 17061358204
    print number
    print bin(number)
    assert option1(number) == option2(number) == 7 
   
