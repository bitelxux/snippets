FILE = "text_23G.txt"

def process_file():
   cont = 0
   with open(FILE) as f:
      for line in f:
          cont += 1
   print cont

if __name__ == "__main__":
  process_file()
