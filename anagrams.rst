Anagrams
========

The problem
------------

Given a words.txt file containing a newline-delimited list of dictionary
words, please implement the Anagrams class so that the get_anagrams() method
returns all anagrams from words.txt for a given word.

**Bonus requirements:**

  - Optimise the code for fast retrieval
  - Write more tests
  - Thread safe implementation

General approach
----------------

*"An anagram is direct word switch or word play, the result of rearranging
the letters of a word or phrase to produce a new word or phrase, using
all the original letters exactly once"* ( source: wikipedia )

That means that in order to get all the anagrams for a needed word, we don't
need to compare the words theirselves but their ordered representation.

Given two words, word1 and word2

If the ordered characters of word1 are the same that the ordered characters
of word2,

Then

word1 and word2 are anagrams.

Assumtions
----------

- Anagrams are **no** case sensitive so "Star" is an anagram of "Tras".
- Special caracters as " ' " are considered as regular caracters too.

Solutions
---------

There is a few options to approach this problem, and this document goes through
some of them, from the one which could come first to an inexperienced
developer's head to a couple of them with important improvements.

Well see that the first approach, wich implements the trivial solution, has
am awful performance, while the second and third one performs thousands of times
better with a cost of some extra memory use.

Solution 1
..........

This approach collects all the words in the dictionary and stores them in a list.
In order to find the anagrams for a given word, the algorithm needs
to sort each of the words in the dictionary to compair them to the
sorted given word.

The building of the list is very fast, as no operation involved.
However, further searchs are very slow due to the dictionary needs to be
complely walked in order to find anagrams.

.. code-block:: python
  :startinline: true
  :linenos: true
  :linenos_offset: true
  :include: anagrams/anagrams.py
  :start-after: # rst-Anagrams0
  :end-before: # rst-Anagrams1

Solution 2
..........

In this solution, a python dictionary is created in order to store a pair
keys - values, where key is the ordered characters representation of each
word in the original dictionary and value is a list containing all the words
in the original dictionary where their ordered characters representation is
the same that the key.

In this case, collecting the words from the original words dictionary is
slightly slower and it requires extra memory ( more or less twice, actually )
but the performance later on, getting the anagrams for a given word is
much better as only indexing the characters ordered representation of the
given word will return all its anagrams.

.. code-block:: python
  :startinline: true
  :linenos: true
  :linenos_offset: true
  :include: anagrams/anagrams.py
  :start-after: # rst-Anagrams1
  :end-before: # rst-Anagrams2

Solution 3
..........

Similarly to solution 2, buils a python dictionary where the key is the
hash of the ordered characters representation for each of the original words
and value is a list containing all words where the hash of their ordered
characters representation matches the key.

This one should be the best approach in performance and the extra memory
used for the keys is fixed to *size of integer* * number of words.

.. code-block:: python
  :startinline: true
  :linenos: true
  :linenos_offset: true
  :include: anagrams/anagrams.py
  :start-after: # rst-Anagrams2
  :end-before: # rst-Tests

Results
-------
