#!/usr/bin/python

import os
import time
import unittest

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

def timing(f):
    def inner(self, *args, **kwargs):
        t0 = time.time()
        result = f(self, *args, **kwargs)
        t = time.time() - t0
        #print "%s.%s: %0.12f" % (self.__class__.__name__, f.__name__, t)
        return t, result
    return inner


# Anagrams0
class Anagrams0:

    def __init__(self):
        self.words = open('words.txt').readlines()
                  
    @timing
    def get_anagrams(self, word):
        anagrams = []
        word = "".join(c for c in sorted(word.lower()))
        for w in self.words:
            if "".join(c for c in sorted(w[:-2].lower())) == word:
                anagrams.append(w[:-2])
	return anagrams
       

# Anagrams1
class Anagrams1:

    def __init__(self):
        self.words = {}
        with open('words.txt') as words:
             for word in words:
                base = word.lower()[:-2]
                key = "".join(c for c in sorted(base))
                self.words.setdefault(key, [])
                self.words[key].append(base)
                  
    @timing
    def get_anagrams(self, word):
        key = "".join(c for c in sorted(word.lower()))
        return self.words.get(key, [])


# Anagrams2
class Anagrams2:

    def __init__(self):
        self.hashes = {}
        with open('words.txt') as words:
             for word in words:
                base = word.lower()[:-2]
                key = hash("".join(c for c in sorted(base)))
                self.hashes.setdefault(key, [])
                self.hashes[key].append(base)
        #pprint.pprint(self.hashes)
                  
    @timing
    def get_anagrams(self, word):
        key = hash("".join(c for c in sorted(word.lower())))
        return self.hashes.get(key, [])


class TestAnagrams(unittest.TestCase):
    anagrams0 = Anagrams0()
    anagrams1 = Anagrams1()
    anagrams2 = Anagrams2()

    def test_statistics(self):

        output = open(os.path.join(CUR_DIR, "anagrams.csv"), 'w')
        output.write("anagrams1,anagrams2\n")
        for i in xrange(200):
            #t0, r0 = anagrams0.get_anagrams('plates')
            self.assertEquals(r0, ['palest', 'pastel', 
                                   'petals', 'plates', 'staple'])
            t1, r1 = self.anagrams1.get_anagrams('plates')
            self.assertEquals(r1, ['palest', 
                                   'pastel', 'petals', 'plates', 'staple'])
            t2, r2 = self.anagrams2.get_anagrams('pastel')
            self.assertEquals(r2, ['palest', 'pastel', 
                                   'petals', 'plates', 'staple'])
            if i < 20:
               continue
            output.write("%f, %f\n" %(t1, t2))
        output.close()  

    def test_anagrams(self):
        t2, r2 = self.anagrams2.get_anagrams('pastel')
        self.assertEquals(r2, ['palest', 'pastel',
                               'petals', 'plates', 'staple'])
          

if __name__ == '__main__':
    unittest.main()
