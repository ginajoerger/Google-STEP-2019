#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:00:44 2019

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

def binary_search(sorted_list, length, key):
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
    fail = "\nElement not found!"
    return fail

def find_subset(string):
    n = len(string)
    arr = []
    final = []
    for i in range(0,n):  
        for j in range(i,n):  
            arr.append(string[i:(j+1)]);  
    for i in arr:
        final.append(i)
    return final

def main():
    m = []
    n = []
    dictionary = open("final.dictionary.words.txt", "r")
    answer = open("answer.dictionary.words.txt", "r")
    
    for z in dictionary:
        new = z.rstrip()
        m.append(new)
    for g in answer:
        new = g.rstrip()
        n.append(new)
        
    dictionary.close()
    answer.close()
    
    ##############
    answers = []
    
    start = input("What are the letters?: ")
    x = [''.join(l) for i in range(len(start),0,-1) for l in combinations(start, i)]
    #x = find_subset(start)
    for i in x:
        sorted_start = sorted(i)
        sorted_start2 = ''.join(sorted_start)
                
        y = binary_search(m, 72270, sorted_start2)
        
        if y != "\nElement not found!":
            found = m.index(y)
            translate = n[found]
            if translate not in answers:
                answers.append(translate)
            
    print(answers)
            #if is_anagram(start, translate) == True:
                #print(translate)     
main()