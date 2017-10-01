class Foo():
  b = "this is b"

foo = Foo()
if not hasattr(foo, 'a'):
   print "OK"
if not getattr(foo, 'a', None):
   print "OK"
b = getattr(foo, "b", None)
print b
