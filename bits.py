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
  for bit in bin(number)[3:]:
      if bit == '1':
         current += 1
      else:
         maximum = max(maximum, current)
         current = 0
  return maximum 

def option2(number):
  """
  This approach use binary switch until the number
  is 0
  """
  maximum = 0
  current = 0
  while number != 0:
    if number % 2 != 0:
       current += 1
    else:
       maximum = max(maximum, current)
       current = 0
    number = number >> 1
  return maximum 

if __name__ == "__main__":

    number = 1091926925308
    assert option1(number) == 11
    assert option2(number) == 11
   
