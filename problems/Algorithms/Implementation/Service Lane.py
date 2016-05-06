#!/bin/python

import sys


n,t = (int(x) for x in raw_input().strip().split(' '))
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = (int(y) for y in raw_input().strip().split(' '))
    print min(width[i:j+1])