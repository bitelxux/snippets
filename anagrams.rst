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


Solutions
---------

There is a few options to approach this problem, and this document goes through
some of them, from the one which could come first to an inexperienced developer
to the best ones.

Well see that the first approach, wich implements the trivial solution, has
am awful performance, while the second and third one performs thousands of times
better with a cost of some extra memory.

Solution 1
..........

.. code-block:: python
  :startinline: true
  :linenos: true
  :linenos_offset: true
  :include: anagrams/anagrams.py
  :start-after: # Anagrams0
  :end-before: # Anagrams1

Solution 1
..........
Solution 1
..........


Conclusions
-----------
