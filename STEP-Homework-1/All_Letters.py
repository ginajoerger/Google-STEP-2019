#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:52:58 2019

@author: ginajoerger
"""
from itertools import combinations

def is_anagram(string1, string2):
    newDict1 = {}
    newDict2 = {}
    
    newList1 = list(string1)
    while ' ' in newList1:
        newList1.remove(' ')
        
    newList2 = list(string2)
    while ' ' in newList2:
        newList2.remove(' ')
        
    for x in newList1:
        newDict1[x] = newList1.count(x)
    for y in newList2:
        newDict2[y] = newList2.count(y)
        
    for z in newDict1.keys():
        if not z in newDict2.keys() or newDict1[z] != newDict2[z]:
            return False
    return True

def binary_search(sorted_list, answer_list, length, key):
    start = 0
    end = length-1
    while start <= end:
        mid = int((start + end)/2)
        #return sorted_list[mid], key
        if key == sorted_list[mid]:
            return sorted_list[mid]
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return sorted_list[mid]

def main():
    start = input("What are the letters?: ")
    #x = [''.join(l) for i in range(len(start),0,-1) for l in combinations(start, i)]
    #for i in x:
    m = []
    n = []
    
    sorted_start = sorted(start)
    sorted_start2 = ''.join(sorted_start)
    dictionary = open("final.dictionary.words.txt", "r")
    answer = open("answer.dictionary.words.txt", "r")
    for i in dictionary:
        new = i.rstrip()
        m.append(new)
    for i in answer:
        new = i.rstrip()
        n.append(new)
            
    y = binary_search(m, n, 72270, sorted_start2)
    
    found = m.index(y)
    translate = n[found]
    
    if is_anagram(start, translate) == True:
        print(translate)
    
    dictionary.close()
    answer.close()
        
main()
    #break down the word into subsets
    #run each subset through binary search algorithm
    #Everytime it finds an answer, make a format for printing (only right side)
    #check if each answer is an anagram
    
    