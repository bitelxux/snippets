#!/bin/sh

anagrams.pdf: anagrams.rst anagrams/anagrams.py anagrams/anagrams.csv
	rst2pdf -e preprocess anagrams.rst | grep -v line 

clean:
	rm -f anagrams.pdf anagrams.png anagrams/anagrams.csv
