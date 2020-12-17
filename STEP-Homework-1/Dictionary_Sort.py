#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:29:22 2019

@author: ginajoerger
"""

def sorting(word):            #Sorts a word alphabetically
    new_word = word.lower()
    a = sorted(new_word)
    return ''.join(sorted(a))

###########
# First, sort individual word in "dictionary.words.txt" alphabetically.
# Append original words into list "orig".
# Append newly sorted individual words to list "alpha", with original words as well.
    
def main():
    original = open('dictionary.words.txt', 'r')
    
    orig = [] #original dictionary
    alpha = [] #words alphabetically sorted
    
    for i in original:
        orig.append(i)
        sort = sorting(i)
        alpha.append(sort + ',' + i)

    original.close()

###########
# Next, sort the entirety of list "alpha" alphabetically, and name it "reorder".
# Write every word into file "final.words.txt", if its length is less than or equal to 16. 

    reorder = sorted(alpha)

    new = open('final.dictionary.words.txt', 'w')
    new2 = open('answer.dictionary.words.txt', 'w')

    for i in reorder:
        left, right = i.split(",")
        length = len(left)
        if length <= 17:
            new.write(left)
            new2.write(right)
    
    new.close()
    new2.close()
    
main()
    