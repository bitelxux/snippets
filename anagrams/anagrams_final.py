#!/usr/bin/python

"""
Given a words.txt file containing a newline-delimited list of dictionary
words, please implement the Anagrams class so that the get_anagrams() method
returns all anagrams from words.txt for a given word.

**Bonus requirements:**

  - Optimise the code for fast retrieval
  - Write more tests
  - Thread safe implementation
"""

import os
import time
import unittest


CUR_DIR = os.path.dirname(os.path.realpath(__file__))

class Anagrams(object):

    def __init__(self, source):
        self.source = source

    def get_anagrams(self, word):
        raise PureVirtualMethod("Pure virtual method. Must be redefined")

# rst-Anagrams3
class Anagrams3(Anagrams):
    """
    Hash keys: Create a python dictionary where for each
    original word in the words dictionary, it stores:
      - key: the hash of the original sorted word
      - value: all the words that once ordered have the same hash.
    """

    def __init__(self, source):
        Anagrams.__init__(self, source)
        self.hashes = {}
        with open(self.source) as words:
            for word in [w[:-2].lower() for w in words]:
                key = hash("".join(c for c in sorted(word)))
                self.hashes.setdefault(key, [])
                self.hashes[key].append(word)

    @timing
    def get_anagrams(self, word):
        key = hash("".join(c for c in sorted(word.lower())))
        return self.hashes.get(key, [])

# rst-Tests
class TestAnagrams(unittest.TestCase):

    source = os.path.join(CUR_DIR, 'words.txt')

    def setUp(self):
        self.anagrams1 = Anagrams1(self.source)
        self.anagrams2 = Anagrams2(self.source)
        self.anagrams3 = Anagrams3(self.source)

    def test_pure_virtual(self):
        class AnagramsX(Anagrams):
            def __init__(self, source):
                Anagrams.__init__(self, source)

        anagrams = AnagramsX(self.source)
        self.assertRaises(PureVirtualMethod, anagrams.get_anagrams, 'pastel')


    def test_exaustive(self):
        """
        This tests tests all anagrams for all words in the given
        dictionary !!
        They are not ran as individual tests because the required resources
        for it would be massive.
        """
        import exhaustive
        exhaustive.test_exhaustive(self)


if __name__ == '__main__':
    unittest.main()
