#!/bin/python

import sys

def decent_number(n):
    rem = n % 3
    threes = ((3 - rem) % 3) * 5
    fives = n - threes
    if fives < 0:
        return -1
    else:
        return int("5"*fives + "3"*threes)
    
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print decent_number(n)
    
    