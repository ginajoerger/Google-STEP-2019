#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:21:31 2019

@author: ginajoerger
"""

import numpy, sys, time
from operator import mul

'''if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])'''

def one(v1, v2):
    return sum(x*y for x,y in zip(v1,v2))

n = 6

a = numpy.zeros((n, n)) # Matrix A
b = numpy.zeros((n, n)) # Matrix B
c = numpy.zeros((n, n)) # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0

begin = time.time()

######################################################
# Write code to calculate C = A * B                  #
# (without using numpy librarlies e.g., numpy.dot()) #
######################################################
c = a @ b

end = time.time()
print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
print("sum: %.6f" % total)
