import os

def tree(directory):
  items = os.listdir(directory)
  for item in items:
      fullpath = os.path.join(directory, item)
      print fullpath
      if os.path.isdir(fullpath):
          tree(fullpath)

if __name__ == "__main__":
    tree("/usr/bin")
