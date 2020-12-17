# STEP-Homework-1
Intro to CS &amp; Git - Anagrams and Lex

Instructions:

1. Make a program that can find single word anagrams that use all the characters in a given string (e.g. “omnsotare” -> “astronomer”)
2. Adapt that program to find anagrams that use only a subset of characters.
    - The way that I described of trying all 2^16 possible subsets will work.
    - Feel free to experiment in ways to do that faster!
3. Try optimizing your choice of anagrams to find the highest scoring one, rather than just the longest one.


Just a quick explanation about the files:

1. "dictionary.words.txt" is the text file with all the original dictionary words from Kris's website.
2. "Dictionary_Sort.py" is the python code used to alphabetically sort each word, and then to sort the entire file itself.
3. "final.dictionary.words.txt" is the text file with the alphabetically sorted words.
4. "answer.dictionary.words.txt" is the text file which unscrambles words in the order of "final.dictionary.words.txt".
5. "All_Letters.py" is the python code used to find only single word anagrams.
6. "Some_Letters.py" is the python code used to find all the subset anagrams, and the one I mainly used to solve the online puzzle.
