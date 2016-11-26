import re

FILE = "book.of.death.txt"
#FILE = "text_23G.txt"

regulars = {
  'four_letters': r"\b\w{4}\b",
  'first_capital': r"(?!\. )\b[A-W][a-w]+\b",
  'all_capitals': r"[A-W]{2,100}\b",
  'romans': r"[ILXVM]{2,10}\b"
}

def process():
  for key, regular_str in regulars.items():
      regular = re.compile(regular_str)
      print "\n\n%s:" % key + "*"*80 + '\n'
      with open(FILE) as f:
        for line in f:
          for match in regular.findall(line):
              print match,

if __name__ ==  "__main__":
  process()
