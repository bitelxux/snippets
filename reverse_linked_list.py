import random

class LinkedList():

    def __init__(self):
       self.head = None

    def walk(self):
       node = self.head
       while node:
          yield node
          node = node.next

    def tail(self):
       node = self.head
       while node and node.next:
          node = node.next
       return node

    def __repr__(self):
       return "->".join(str(node.value) for node in self.walk())

    def add(self, value):
       node = Node(value)
       if not self.head:
          self.head = node
       else:
          self.tail().next = node

    def reverse(self, head):

      current = head
      previous = None

      while current:
         next = current.next
         current.next = previous
         previous = current
         current = next

      self.head = previous

    def recursive_reverse(self, current):
      if current is None:
         return

      if current.next is None:
         self.head = current
         return

      self.recursive_reverse(current.next)
      current.next.next = current
      current.next = None
         

class Node():

    def __init__(self, value):
      self.value = value
      self.next = None
       

if __name__ == "__main__":
   llist = LinkedList()
   for i in range(1, 3):
       llist.add(i)
   print llist
   print "---"

   #llist.reverse(llist.head)
   #print llist
   llist.recursive_reverse(llist.head)
   print llist


